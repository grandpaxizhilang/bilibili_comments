import json
import scrapy
from loguru import logger
import time
import re
import hashlib
import urllib.parse
from datetime import datetime
import math
import requests
from urllib.parse import urlencode
from Scarpy.bilibili_comments.bilibili_comments.items import BilibiliCommentsItem
from Scarpy.bilibili_comments.bilibili_comments.settings import BV
from Scarpy.bilibili_comments.bilibili_comments.settings import COOKIES
from Scarpy.bilibili_comments.bilibili_comments.settings import HEADERS
from Scarpy.bilibili_comments.bilibili_comments.settings import father_time


class CommentsCrawlSpider(scrapy.Spider):
    name = 'comments_crawl'
    allowed_domains = ['bilibili.com/','api.bilibili.com']
    start_urls = 'http://www.bilibili.com/'
    # 父评论区url
    url_main = 'https://api.bilibili.com/x/v2/reply/wbi/main?'
    # 视频id
    oid = ''
    # 储存子评论区的root
    roots = []



    def md5_encode(self, s):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        return m.hexdigest()

    def encode_uri_component(self, s):
        return urllib.parse.quote(s, safe='~()*!.\'')

    def get_rid(self, data):
        H = 'ea1db124af3c7062474693fa704f4ff8'
        q = sorted(data.keys())
        ne = []
        te = re.compile(r"[!'()*]")
        for oe in range(len(q)):
            le = q[oe]
            de = data[le]
            if de and type(de) == 'str':
                de = te.sub("", de)
            if le == 'pagination_str':
                ne.append(f"pagination_str={self.encode_uri_component(de)}")
            else:
                ne.append(f'{le}={de}')
        ee = '&'.join(ne)
        w_rid = self.md5_encode(ee + H)
        return w_rid


    # 返回数据并且进行对子评论进行请求
    def get_father_comment(self,comments):
        items = BilibiliCommentsItem()
        for i in range(len(comments['data']['replies'])):
            uid = comments['data']['replies'][i]['mid_str']
            content = comments['data']['replies'][i]['content']['message']
            date = datetime.fromtimestamp(comments['data']['replies'][i]['ctime']).strftime('%Y-%m-%d')
            # 这里判断有没有回复，如果不是空数组就存入root，并且把数据存到父评论区的列表中
            if comments['data']['replies'][i]['replies']:
                root = comments['data']['replies'][i]['rpid_str']
                # 对子评论区进行请求
                # if root:
                #     yield
                items['uid'] = uid
                items['content'] = content
                items['date'] = date
                items['father'] = ''
                items['child'] = root
                yield items
            else:
                items['uid'] = uid
                items['content'] = content
                items['date'] = date
                items['father'] = ''
                items['child'] = ''
                yield items



    # 第一次请求页面（这里可以进行多个视频的评论区进行爬取），生成oid
    def start_requests(self):
        for i,bv in enumerate(BV):
            url = self.start_urls + bv
            yield scrapy.Request(url=url,cookies=COOKIES,headers=HEADERS,callback=self.parse)

    # 这里实现了父评论区的全部爬取
    def parse(self, response):
        session = requests.session()
        # 获取视频的oid
        self.oid = response.text.split('"aid":')[1].split(',')[0]
        logger.info('生成的oid:' + self.oid)
        flag = 1
        while True:
            time.sleep(father_time)
            # 这里只访问一次第一页
            if flag:
                params = {
                    "oid": self.oid,
                    "type": '1',
                    "mode": '3',
                    "pagination_str": "{\"offset\":\"\"}",
                    "plat": '1',
                    "seek_rpid": "",
                    "web_location": "1315875",
                    "wts": int(time.time())
                }
                # 生成加密参数
                w_rid = self.get_rid(params)
                params['w_rid'] = w_rid
                response = session.get(url=self.url_main, headers=HEADERS, params=params, cookies=COOKIES)
                flag = 0
            else:
                params_next = {
                    "oid": self.oid,
                    "type": "1",
                    "mode": "3",
                    "pagination_str": "{\"offset\":\"{\\\"type\\\":1,\\\"direction\\\":1,\\\"session_id\\\":\\\"1756344138195927\\\",\\\"data\\\":{}}\"}",
                    "plat": "1",
                    "web_location": "1315875",
                }
                params = params_next.copy()
                params["wts"] = int(time.time())
                w_rid = self.get_rid(params)
                params['w_rid'] = w_rid

                # 发送请求
                response = session.get(url=self.url_main, headers=HEADERS, params=params, cookies=COOKIES)

            comments = json.loads(response.text)
            # 如果有评论
            if comments['data']['replies']:
                print(comments)
                self.get_father_comment(comments)
            else:
                break



    # 获取所有的子评论
    def parse_child(self,response):
        pass




