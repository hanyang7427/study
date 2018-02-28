# 抓取http://www.xicidaili.com/中的代理服务器的
# IP，Port取出来，保存到本地文件中；

# import urllib.request
# url = 'http://www.xicidaili.com/'
# ua_headers = {
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
# "Connection":"keep-alive",
# "Host":"www.xicidaili.com",
# "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
# }
# requset = urllib.request.Request(url,headers=ua_headers)
# html = urllib.request.urlopen(requset)
# html = html.read().decode('utf-8')

# 正则提取html数据
import re
L = []
with open('proxy_list.html') as f:
    pat = re.compile('<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d{1,5})</td>[\s\S]*?<td>(\w*?)</td>')
    result = re.findall(pat,f.read())
for x,y,z in result:
    L.append({'IP':x,'PORT':y,'city':z})

with open('proxy_list.txt','w') as f:
    for i in L:
        f.write(str(i)+'\n')