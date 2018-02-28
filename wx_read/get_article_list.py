# -*- coding: utf-8 -*-
import requests
import time
import json
import csv
import re
from urllib.parse import urlparse
from urllib.parse import parse_qs

def ts2dt(value):
    format = '%Y-%m-%d'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

def url2dict(url):
    query = urlparse(url).query
    return dict([(k, v[0]) for k, v in parse_qs(query).items()])
# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
  "Cookie": 'pgv_pvid=9447690576; pgv_pvi=2952456192; RK=ke0XqQyKGt; ptcz=c90139b1cec1bd42263dd4aae694dd126287dbb91f72ae9e63b3ff7fb2338438; pt2gguin=o0610654342; ptui_loginuin=610654342@qq.com; o_cookie=610654342; ua_id=UClY4DzZeqBUBNP3AAAAAM_D7wSLDHY0_FNR65mG33o=; mm_lang=zh_CN; pgv_si=s8107379712; uuid=75fcf6c8fecec2dbdc40380b28204f8b; ticket=940468c38c747be83c04501af52d0b159a2dee2d; ticket_id=gh_dd4388b51378; cert=hhguJrcIBMWBcKV4BFPFL5kRjHU5lRsz; noticeLoginFlag=1; data_bizuin=3228629589; bizuin=3203628953; data_ticket=eISHpfsxpeSJBBd2dliRHaRgJlQ6psAjAU3QYahZ2MunaKHpVgPkxS+J/49m/Qc4; slave_sid=VVI4alFaRDhVU21Zb3BpNWhVaGJxN3h2c2RSMW80ZHRPZHJCVV9WSmprRTUwWk9rX3FJdnBpNVRWZWFfVXZIMVFudHlXem5TRnNDX0RrM3RydVl2bEF2akZ3TGZCSXZPQlV5X3A2aXIxNHVOSXJvS1plcGNwSE9LUXlHT3FVRDEybDVra3R1OTZjWm5IcVJp; slave_user=gh_dd4388b51378; xid=4bd981a745754e979ef9e90c37c39fde; openid2ticket_oVfpwwK8m8TLtRsykDrmm3PoRcsE=0fvFCO4CECpf1FYXcLV10X/z3e9KImIRdOBRuCASjTI=; rewardsn=',
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
}

"""
需要提交的data
以下个别字段是否一定需要还未验证。
注意修改yourtoken,number
number表示从第number页开始爬取，为5的倍数，从0开始。如0、5、10……
token可以使用Chrome自带的工具进行获取
fakeid是公众号独一无二的一个id，等同于后面的__biz
"""
data = {
    "token": 1524985860,
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": 0,
    "count": "5",
    "query": "",
    "fakeid": 'MjM5NjEzNDQ2Mg==',
    "type": "9",
}
for i in range(200):
    # 使用get方法进行提交
    content_json = requests.get(url, headers=headers, params=data).json()
    # 返回了一个json，里面是每一页的数据
    with open('article_of_wan.csv', 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for item in content_json["app_msg_list"]:
            # 提取每页文章的标题及对应的url
            if re.match(r'^\d+?_1$',item["aid"]):
                writer.writerow([
                    (item["title"][1:5] + "..." +item["title"][-4:]).replace(',',''),
                    url2dict(item["link"])['__biz'] + ' ' +
                    url2dict(item["link"])['mid'] + ' ' +
                    url2dict(item["link"])['sn'],
                    ts2dt(item["update_time"])])
    data['begin'] += 5
    time.sleep(20)