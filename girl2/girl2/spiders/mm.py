# -*- coding: utf-8 -*-
import hashlib
import os
import time

import scrapy
from scrapy import Request
from scrapy.settings.default_settings import CLOSESPIDER_ITEMCOUNT, CLOSESPIDER_PAGECOUNT


class MmSpider(scrapy.Spider):
    name = 'mm'
    allowed_domains = ['mm.enterdesk.com']
    start_urls = ['https://mm.enterdesk.com/bizhi/29134-188716.html']


    def parse(self, response):
        item = {}
        nodes = response.css('.swiper-wrapper .swiper-slide')
        page = 1
        # num = 0
        for node in nodes:
            item['img'] = node.css('a').xpath('./img/@src').get()
            item['name'] = '高清美女壁纸' + str(page)
            # item['images'] = []
            page += 1
            # num += 1
            # if num == 8 :
            #     break
            yield item
# if __name__ == '__main__':
#     while True:
#         os.system('scrapy crawl mm -o mmmm.csv')
#         time.sleep(120)

