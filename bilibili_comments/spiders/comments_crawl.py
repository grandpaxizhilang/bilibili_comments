import scrapy


class CommentsCrawlSpider(scrapy.Spider):
    name = 'comments_crawl'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    def parse(self, response):
        pass
