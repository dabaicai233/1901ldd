# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from csv import DictWriter

import pymysql

from qiushibaike import settings


class QiushibaikePipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(**settings.DB_CONFIG)

    def process_item(self, item, spider):
        sql = 'insert into dl(name, img, text)values(%(name)s, %(img)s, %(text)s)'
        with self.conn as c:
            c.execute(sql, args=dict(item))
        return item
