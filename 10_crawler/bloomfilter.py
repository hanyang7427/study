# -*- coding:utf-8 -*-
# git clone https://github.com/axiak/pybloomfiltermmap.git
# python setup.py install
# 使用python2执行
import pybloomfilter

# 定义一个BloomFilter， 0.1->error rate
fruit = pybloomfilter.BloomFilter(1024*1024*16, 0.1)

# fruit在爬虫中都是一个URL
#fruit.update(('apple', 'pear', 'orange', 'apple'))
fruit.add('strawberry')
print(len(fruit))

element = raw_input("Please input your fruit:")
if element in fruit:
    print("is exist")
else:
    fruit.add(element)
    print(len(fruit))
#print('mike' in fruit)
#print(fruit.__contains__('mike'))
##False
#print('apple' in fruit)
##True