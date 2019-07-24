# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from xiaohua.items import ThumbItem
import pymysql
from xiaohua import settings

class XiaohuaPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(**settings.DB_CONFIG)

    def process_item(self, item, spider):
        if isinstance(item,ThumbItem):
            #  普通页面的sql语句
            sql = 'INSERT INTO thumb_item(id, name, info_url, img_url, width, height) ' \
                  'values(%(id)s,%(name)s,%(info_url)s,%(img_url)s,%(width)s,%(height)s)'
        else:
            # 详情页面的sql语句
            item['images'] =os.path.join(settings.IMAGES_STORE, item['images'][0].get('path'))

            sql = 'insert into item_info(uid,img_url) ' \
                  'values(%(uid)s,%(images)s)'

        # 将item数据保存到数据库中
        # python上下文，使用with关键字，如果哪一个对象使用了with，
        # 则这个对象的类必须实现__enter_()和__exit__()两个函数。
        #  __enter__()是进入上下文时调用的函数，一般返回相应的对象
        #  __exit__(self,exc_type,exc_val,exc_tb)
        #       当对象退出上下文时调用的函数，用于回收资源
        with self.conn as c:

            # args 可以是元组，对应是sql语句中的 %s
            # 也可以是字典，对应的是sql语句中的%(key)s
            c.execute(sql,args=dict(item))

        self.conn.commit()
        return item
