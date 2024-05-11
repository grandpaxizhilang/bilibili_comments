import json
import scrapy
from loguru import logger
import time
import re
import hashlib
import urllib.parse
from datetime import datetime
import math
from urllib.parse import urlencode
from Scarpy.bilibili_comments.bilibili_comments.items import BilibiliCommentsItem
from Scarpy.bilibili_comments.bilibili_comments.settings import BV
from Scarpy.bilibili_comments.bilibili_comments.settings import COOKIES
from Scarpy.bilibili_comments.bilibili_comments.settings import HEADERS



class CommentsCrawlSpider(scrapy.Spider):
    name = 'comments_crawl'
    allowed_domains = ['bilibili.com/','api.bilibili.com']
    start_urls = 'http://www.bilibili.com/'
    oid = ''

    def md5_encode(self,s):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        return m.hexdigest()

    def encode_uri_component(self,s):
        return urllib.parse.quote(s, safe='~()*!.\'')

    def get_rid(self,data):
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



    def get_father_comment(self,comments):
        items = BilibiliCommentsItem()
        for i in range(len(comments['data']['replies'])):
            uid = comments['data']['replies'][i]['mid_str']
            content = comments['data']['replies'][i]['content']['message']
            date = datetime.fromtimestamp(comments['data']['replies'][i]['ctime']).strftime('%Y-%m-%d')
            # 这里判断有没有回复，如果不是空数组就存入root，并且把数据存到父评论区的列表中
            if comments['data']['replies'][i]['replies']:
                root = comments['data']['replies'][i]['rpid_str']
                roots.append(root)
                father_data.append((uid, content, date, '', root))
            else:
                father_data.append((uid, content, date, '', ''))





    # 第一次请求页面（这里可以进行多个视频的评论区进行爬取），生成oid
    def start_requests(self):
        for bv in BV:
            url = self.start_urls + bv
            yield scrapy.Request(url=url,cookies=COOKIES,headers=HEADERS,callback=self.parse)


    def parse(self, response):
        # 获取视频的oid
        self.oid = response.text.split('"aid":')[1].split(',')[0]
        url = 'https://api.bilibili.com/x/v2/reply/wbi/main?'
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
        logger.info(params)
        # 生成加密参数
        w_rid = self.get_rid(params)
        params['w_rid'] = w_rid
        url += urlencode(params)
        logger.info(url)
        yield scrapy.Request(url=url,cookies=COOKIES,headers=HEADERS,callback=self.parse_next)

    # 获取下一页的父评论
    def parse_next(self,response):
        # 获取评论
        comments = json.loads(response.text)
        self.get_father_comment(comments)



        logger.success(response)
        yield {}





