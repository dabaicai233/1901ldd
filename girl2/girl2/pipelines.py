# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import time

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class Girl2Pipeline(object):
    def process_item(self, item, spider):

        print('=============', item)
        return item


class MmImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x,meta={'name': item['name']}) for x in item.get('img', [])]
        # print('=========',item.get('img'))

    def file_path(self, request, response=None, info=None):
        name = request.meta.get('name')

        return 'girls/%s.jpg' % name


