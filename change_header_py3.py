from urllib.request import urlopen
from urllib.request import Request
import os

# GET /aid17071201am/aid17071201am.m3u8 HTTP/1.1
# Host: videotts.it211.com.cn
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0
# Accept: */*
# Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
# Accept-Encoding: gzip, deflate
# Referer: http://tts.tmooc.cn/video/showVideo?menuId=583341&version=AID_V02
# Origin: http://tts.tmooc.cn
# Connection: close

# GET /aid17071201am/static.key HTTP/1.1
# Host: videotts.it211.com.cn
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0
# Accept: */*
# Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
# Accept-Encoding: gzip, deflate
# Referer: http://tts.tmooc.cn/video/showVideo?menuId=583341&version=AID_V02
# Origin: http://tts.tmooc.cn
# Connection: close

# GET /aid17071201am/aid17071201am-0.ts HTTP/1.1
# Host: videotts.it211.com.cn
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0
# Accept: */*x
# Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
# Accept-Encoding: gzip, deflate
# Referer: http://tts.tmooc.cn/video/showVideo?menuId=583341&version=AID_V02
# Origin: http://tts.tmooc.cn
# Connection: close

days = ['1113','1114','1115','1118','1120','1121','1122']
sources = [y+x for x in ('am','pm') for y in days]
print(sources)
ua_headers = {
    "Host": "videotts.it211.com.cn",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://tts.tmooc.cn/video/showVideo?menuId=583341&version=AID_V02",
    "Origin": "http://tts.tmooc.cn",
    "Connection": "close",
}

# for i in sources:
#     os.mkdir(i)

paths = []
for source in sources:
    paths.append(os.path.join(source,'aid1707'+source+'.m3u8'))
for i in paths:
    with open(i,'wb') as f:
        req = Request('http://videotts.it211.com.cn/aid1707{}/aid1707{}.m3u8'.format(os.path.dirname(i),os.path.dirname(i)),
                      headers=ua_headers)
        print('http://videotts.it211.com.cn/aid1707{}/aid1707{}.m3u8'.format(os.path.dirname(i),os.path.dirname(i)))
        res = urlopen(req)
        f.write(res.read())

