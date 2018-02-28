# 抓取豆瓣中top100电影数据，
#  入口：
#  https://movie.douban.com/j/chart/top_list?type=10&interval_id=100:90&action
#  post:
#     {"start":"0","end":"100"}
# 解析json数据，保存到本地文件中

import urllib.request
import urllib.parse
import json
url = "https://movie.douban.com/j/chart/top_list?type=10&interval_id=100:90&action"
ua_headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
formdata = {"start":"150","end":"150"}
post_data = urllib.parse.urlencode(formdata)
post_data = bytes(post_data.encode('utf-8'))
request = urllib.request.Request(url,data=post_data,headers=ua_headers)
html = urllib.request.urlopen(request)
result = json.loads(html.read().decode('utf-8'))

with open('douban.txt','w') as f:
    for i in result:
        f.writelines(str(i)+'\n')