# -*- coding:utf-8 -*-
import urllib2

#独享代理IP地址	端口号
#114.67.143.11	16816
#用户名：394996257密码：a1jnn6er
import re

def checkProxy(htmlInfo):
    data = re.compile('<title>百度一下，你就知道</title>')
    ti = re.findall(data, htmlInfo)
    if ti is None:
        return False
    else:
        return True

# 设置代理服务器的信息
#user = "394996257fadsfas"
#passwd = "a1jnn6er1234"
#proxyServer = "114.67.143.114:16816"
#passInfo = urllib2.HTTPPasswordMgrWithDefaultRealm()
#passInfo.add_password(None, proxyServer, user, passwd)

# 构造一个proxy handler来处理http
#proxy_handler = urllib2.ProxyBasicAuthHandler(passInfo)
proxy_hanlder2 = urllib2.ProxyHandler({"http":"394996257:a1jnn6er@114.67.143.11:16816"})
http_opener = urllib2.build_opener(proxy_hanlder2)

request = urllib2.Request("http://www.bing.com")
response = http_opener.open(request)
#print(response.read())
print(checkProxy(response.read()))

#with open("baidu1.html", "w") as f:
#      f.write(response.read())