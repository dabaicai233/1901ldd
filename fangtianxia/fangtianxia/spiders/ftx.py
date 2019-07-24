# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class FtxSpider(scrapy.Spider):
    name = 'ftx'
    allowed_domains = ['xian.newhouse.fang.com']
    start_urls = ['https://xian.newhouse.fang.com/house/s/']

    def parse(self, response):
        item = {}
        f_nodes = response.css('.nlc_details')
        for f_node in f_nodes:
            item['name'] = "".join((f_node.css('.nlcd_name').xpath('./a/text()').get()).split())
            item['address'] = f_node.css('.address').xpath('./a/@title').get()
            item['phone'] = f_node.css('.tel').xpath('./p/text()').get()
            item['sign'] = f_node.css('.fangyuan ').\
                xpath('./span/text() | ./a[1]/text() | ./a[2]/text() | ./a[3]/text() | ./a[4]/text()').extract()
            item['type'] = f_node.css('.house_type').xpath('./a/text()').extract()
            item['price'] = f_node.css('.nhouse_price').xpath('./span/text() | ./em/text()').extract()

            yield item

        next_url = response.css('.page').xpath('.//li/a[last()-1]/a/@href').get()
        yield Request(next_url,callback=self.parse,priority=10,dont_filter=True)