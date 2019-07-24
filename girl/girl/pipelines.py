# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from girl import settings


class GirlPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(**settings.DB_CONFIG)

    def process_item(self, item, spider):
        sql = 'insert into girls(img, name)values(%(img)s, %(name)s)'
        with self.conn as c:
            c.execute(sql, args=dict(item))
        return item
