# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        item = {}
        content_nodes = response.css('.article ')
        for content_node in content_nodes:
            item['name'] = content_node.css('.author').xpath('./a/img/@alt').get()
            item['img'] = content_node.css('.author').xpath('./a/img/@src').get()
            item['text'] = "".join((content_node.css('.content').xpath('./span/text()').get()).split())
            yield item

        next_url = response.css('.pagination').xpath('.//li[last()]/a/@href').get()
        yield Request('https://www.qiushibaike.com' + next_url,callback=self.parse,priority=10,dont_filter=True)
