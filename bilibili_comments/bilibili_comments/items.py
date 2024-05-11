# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliCommentsItem(scrapy.Item):
    # 用户uid
    uid = scrapy.Field()
    # 回复内容
    content = scrapy.Field()
    # 评论时间
    date = scrapy.Field()
    # 父标识
    father = scrapy.Field()
    # 子标识
    child = scrapy.Field()

