# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class DailiSpider(RedisCrawlSpider):
    name = 'daili'
    allowed_domains = ['www.kuaidaili.com']
    # start_urls = ['http://www.kuaidaili.com/']
    redis_key = 'dl:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'https://www.kuaidaili.com/free/inha/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        node_urls = response.css('#list>table>tbody')
        for node_url in node_urls:
            item['ip'] = node_url.xpath('./tr/td[1]/text()').get()
            item['port'] = node_url.xpath('./tr/td[2]/text()').get()
            item['ip_type'] = node_url.xpath('./tr/td[4]/text()').get()
            item['pri_time'] = node_url.xpath('./tr/td[7]/text()').get()

            yield item
