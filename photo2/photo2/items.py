# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Photo2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #id = scrapy.Field()
    #title = scrapy.Field()
    img_info = scrapy.Field()
    name = scrapy.Field()


class TPItem(scrapy.Item):
    uid = scrapy.Field()
    images = scrapy.Field()
    imgs = scrapy.Field()
    name = scrapy.Field()
