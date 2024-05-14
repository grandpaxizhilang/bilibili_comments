# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from loguru import logger
from Scarpy.bilibili_comments.bilibili_comments.settings import MYSQL
from Scarpy.bilibili_comments.bilibili_comments.settings import PATH


# 存储csv的管道
class CSV_Pipeline:

    def open_spider(self,spider):
        path = PATH + '评论区数据.csv'
        self.fp = open(path,'a',encoding='utf-8')


    def close_spider(self,spider):
        if self.fp:
            self.fp.close()

    def process_item(self, item, spider):

        self.fp.write(f"{item['uid']},{item['content']},{item['date']},{item['father']},{item['child']}\n")
        return item


class MYSQL_Pipeline:

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host=MYSQL['host'],
            port=MYSQL['port'],
            user=MYSQL['user'],
            password=MYSQL['password'],
            database=MYSQL['database']
        )

    def close_spider(self,spider):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        # try:
        #     cursor = self.conn.cursor()
        #     sql = 'insert into bilibili_comments (uid, content, date, father, child) values (%s, %s, %s, %s, %s)'
        #     cursor.executemany(sql, (item['uid'],item['content'],item['date'],item['father'],item['child']))
        #     self.conn.commit()
        # # except:
        # #     logger.debug('数据库存入失败:'+ f"{item['uid']},{item['content']},{item['date']},{item['father']},{item['child']}")
        # #     self.conn.rollback()
        # finally:
        #     if cursor:
        #         cursor.close()

        cursor = self.conn.cursor()
        sql = 'insert into bilibili_comments (uid, content, date, father, child) values (%s, %s, %s, %s, %s)'
        cursor.execute(sql, (item['uid'],item['content'],item['date'],item['father'],item['child']))
        self.conn.commit()

        return item