# -*- coding: utf-8 -*-
import hashlib

import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

from photo2.items import TPItem


class Ph2Spider(scrapy.Spider):
    name = 'ph2'
    allowed_domains = ['www.883mz.com']
    start_urls = ['https://www.883mz.com/pic/2/']

    def parse(self, response):
        item = {}
        nodes = response.css('.channel>ul>li')
        for node in nodes:
            item['name'] = node.css('a').xpath('./text()').get()
            item['img_info'] = 'https://www.883mz.com/' + node.css('a').xpath('./@href').get()

            item['id'] = hashlib.md5(item['img_info'].encode()).hexdigest()
            yield item
            yield Request(item['img_info'], callback=self.parse_info,
                          meta={'uid':item['id'], 'name': item['name']}, priority=10)

    def parse_info(self, response: HtmlResponse):
        item = TPItem()
        # photos = response.css('.content>p>img')
        # print(photos)
        # for photo in photos:
        item['uid'] = response.meta.get('uid')
        item['name'] = response.meta.get('name')
        item['imgs'] = response.css('.content>p>img').xpath('./@src').extract()
        item['images'] = []
        yield item

