# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    #职位名称    职位类别    人数  地点  发布时间
    positionName = scrapy.Field()
    #postionLink = scrapy.Field()
    positionType = scrapy.Field()
    pNum = scrapy.Field()
    address = scrapy.Field()
    publishTime = scrapy.Field()

