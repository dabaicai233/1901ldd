# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

from xiaohua.items import ThumbItem,XHItem
import hashlib

class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['www.521609.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/list32.html']

    def parse(self, response):
        # 获取所有图片所在的li节点
        li_nodes = response.css('.index_img>ul>li')

        item = ThumbItem()
        for li_node in li_nodes:
            # 从li_node 节点提取图片路径、个人详情页和用户名
            item['info_url'] = 'http://www.521609.com' + li_node.css('a').xpath('./@href').get()
            item['width'],item['height'],item['name'] = li_node.css('a>img').xpath('./@width | ./@height | ./@alt').extract()
            item['img_url'] = 'http://www.521609.com' + li_node.css('a>img').xpath('./@src').get()

            # 通过md5将info_url转成32位长度的字符串
            item['id'] = hashlib.md5(item['info_url'].encode()).hexdigest()
            yield item

            # 发起详情页面的请求。优先级高一些（数值低）
            yield Request(item['info_url'],
                          callback=self.parse_info,
                          meta={'uid': item['id']},
                          priority=10)

            # 下一页
            next_url = 'http://www.521609.com/daxuexiaohua/' + response.css('.listpage').xpath('.//li[last()-2]/a/@href').get()
            # 发起下一页请求，优先级低一些（数值高）
            yield Request(next_url,priority=10,dont_filter=False)

    def parse_info(self,response:HtmlResponse):
        item = XHItem()

        # 从请求对象中传入meta对象中的uid数据
        item['uid'] = response.meta.get('uid')
        item['image_urls'] = ['http://www.521609.com' + response.css('#bigimg').xpath('./@src').get()]
        item['images'] = []
        yield item
        # 下一页url
        next_url = response.css('.pagelist').xpath('./li[last()]/a/@href').get()
        if next_url != '#':
            next_url = 'http://www.521609.com/daxuexiaohua/'+ next_url
            yield Request(next_url,callback=self.parse_info,
                          meta={'uid': item['uid']},
                          priority=10)