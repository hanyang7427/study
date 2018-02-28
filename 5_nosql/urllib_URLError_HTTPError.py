from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
def get_title(url):
    '''
    HTTPError:请求已经到达web服务器，http状态码是web服务器返回的v
            HTTP状态码，404,500...
    URLERROR:请求没有到达服务器
            三种可能：
                1)无网络连接
                2)连接不到特定服务器
                3)服务器不存在
    '''
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        html = urlopen(url)
    except URLError as e:
        print(e)
        return None
    try:
        bsobj = BeautifulSoup(html.read(),'lxml')
        title = bsobj.body.h1
        return title
    except AttributeError:
        '''
        AttributeError:属性错误，试图获得一个HTML标签，但是该标签不存在，BS4返回一个空对象，并且抛出AttributeError异常
        '''
        return None
title = get_title('http://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title not found')
else:
    print(title)