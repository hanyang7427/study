# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from ..items import TencentspiderItem
#from tencentSpider.items import TencentspiderItem
from scrapy.spiders import CrawlSpider,Rule

#/html/body/div[3]/div[1]/table/tbody/tr[2]
#/html/body/div[3]/div[1]/table/tbody/tr[2]/td[1]/a
#/html/body/div[3]/div[1]/table/tbody/tr[2]/td[2]
#/html/body/div[3]/div[1]/table/tbody/tr[2]/td[3]
#/html/body/div[3]/div[1]/table/tbody/tr[2]/td[4]
#/html/body/div[3]/div[1]/table/tbody/tr[2]/td[5]
class TecentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?start=0#a']
    for i in range(274):
        strI = str(i*10)
        start_urls.append("http://hr.tencent.com/position.php?start="+strI+"#a")
    # start_urls = ['http://hr.tencent.com/position.php?start=0#a',
    #               'http://hr.tencent.com/position.php?start=10#a',
    #               'http://hr.tencent.com/position.php?start=20#a',
    #               'http://hr.tencent.com/position.php?start=20#a',]


    pageLink = LinkExtractor(allow=("start=\d+"))
    # 获取列表里链接,依次发出请求，通过callback依次处理
    rules = [
        Rule(pageLink, callback="parse", follow=True)
    ]

    def parse(self, response):
        for it in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentspiderItem()
            #print(type(item))
            item['positionName'] = it.xpath("./td[1]/a/text()").extract()[0]
            item['positionType'] = it.xpath("./td[2]/text()").extract()[0]
            item['pNum'] = it.xpath("./td[3]/text()").extract()[0]
            item['address'] = it.xpath("./td[4]/text()").extract()[0]
            item['publishTime'] = it.xpath("./td[5]/text()").extract()[0]

            yield item