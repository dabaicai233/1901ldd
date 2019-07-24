# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from daili2 import settings


class Daili2Pipeline(object):
    # def __init__(self):
    #     self.conn = pymysql.Connect(**settings.DB_CONFIG)
    #
    def process_item(self, item, spider):
    #     sql = 'insert into dl(ip, port, ip_type, pri_time)values(%(ip)s, %(port)s, %(ip_type)s, %(pri_time)s)'
    #
    #     with self.conn as c:
    #         c.execute(sql, args=dict(item))
        return item
