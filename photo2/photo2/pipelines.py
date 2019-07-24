# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class Photo2Pipeline(object):
    def process_item(self, item, spider):
        return item


class TPImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'name': item['name']})
                for x in item.get('imgs', [])]

    def file_path(self, request, response=None, info=None):
        image_guid = hashlib.sha1(request.url.encode()).hexdigest()
       # print(image_guid)
       #  name = request.meta.get('name')
        return '%s/%s.jpg' % ('mn_photo', image_guid)
