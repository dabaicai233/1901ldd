# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E6%97%A5%E7%94%A8%E5%93%81&enc=utf-8&suggest=2.'
                  'def.0.V02--12s0,20s0,38s0&wq=riyp&pvid=b47f313f821d4f50889cdccef03936ce']

    def parse(self, response):
        item = {}
        jd_nodes = response.css('.gl-i-wrap')
        for jd_node in jd_nodes:
            item['info_url'] = jd_node.css('.p-img a').xpath('./@href').get()
            item['img'] = jd_node.css('.p-img a img').xpath('./@src').get()
            item['price'] = jd_node.css('.p-price strong').xpath('./i/text()').get()
            item['text'] = jd_node.css('.p-name em').xpath('./text()').get()
            item['store'] = jd_node.css('.J_im_icon a').xpath('./text()').get()
            yield item
            yield Request(item['info_url'],callback=self.parse_info,priority=10)

    def parse_info(self,response: HtmlResponse):
        item = {}
        item['talks'] = response.css('.cmt_list li').xpath('./cmt_cnt/text()').extract()
        yield item