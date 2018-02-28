# -*- coding:utf-8 -*-
import random
# import urllib
# import urllib2
import urllib.request
import re


# 使用一个user_agent list
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
]
# 随机的从列表里面取出一个user_agent
# user_agent = random.randint(0, len(ua_list) - 1)
user_agent = random.choice(ua_list)

myheaders = {'user_agent': user_agent}
# 构造一个reques请求,把得到的user_agent加进去
# res = urllib2.request.get('https://www.baidu.com', headers=myheaders)
res = urllib.request.Request('http://www.baidu.com', headers=myheaders)
# 访问百度首页，查看<title>百度一下，你就知道</title>
response = urllib.request.urlopen(res)
html = response.read().decode('utf-8')
data = re.compile('<title>百度一下，你就知道</title>')
ti = re.findall(data, html)
# 打印当前的user-agent是什么
print(user_agent)
print(ti)
# 保存下载到的百度首页，或者在提取到的网页中检测是否有
with open('baidutest.html', 'w') as f:
    f.write(html)
 # <title>百度一下，你就知道</title>