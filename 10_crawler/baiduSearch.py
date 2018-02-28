# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
# https://www.baidu.com/s?wd=python

ua_headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"}


url = "http://www.baidu.com/s"
keyword = input("请输入你要查询的信息:")
wd = {"wd":keyword}
wd = urllib.parse.urlencode(wd)   # 'wd=keyword'
fullUrl = url + "?" + wd

request = urllib.request.Request(fullUrl,headers=ua_headers)

# print(request.get_header())
response = urllib.request.urlopen(request)

html = response.read()
with open("baidusearch.html","w") as f:
    f.writelines(html)

#print(html)
print(response.getcode())
print(response.info())
