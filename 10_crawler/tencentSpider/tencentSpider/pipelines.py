# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TencentspiderPipeline(object):
    def __init__(self):
        self.f = open("tecentHR.json","w")

    def process_item(self, item, spider):
        #print("process_item")
        # 存储item信息到json中
        text = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.f.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        #print("close_spider")
        self.f.close()
