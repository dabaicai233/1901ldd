# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 在item.py文件中定义不同的页面提取不同的数据的item类
# item类，封装成了字典的类
import scrapy


class ThumbItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    info_url = scrapy.Field()
    img_url = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()


class XHItem(scrapy.Item):
    uid = scrapy.Field()
    image_urls =scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()