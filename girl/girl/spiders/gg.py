# -*- coding: utf-8 -*-
import scrapy


class GgSpider(scrapy.Spider):
    name = 'gg'
    allowed_domains = ['mm.enterdesk.com']
    start_urls = ['https://mm.enterdesk.com/bizhi/29134-188716.html']

    def parse(self, response):
        item = {}
        nodes = response.css('.swiper-wrapper .swiper-slide')
        page = 1
        for node in nodes:
            item['img'] = node.css('a').xpath('./img/@src').extract()
            item['name'] = '高清美女壁纸' + str(page)
            item['images'] = []
            page += 1
            yield item
