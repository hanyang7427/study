# -*- coding:utf-8 -*-
from multiprocessing import Pool
import requests    # python3
from requests.exceptions import RequestException
import re
import json

def get_one_page(url):
    headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    }
    try:
        response = requests.get(url, headers=headers)
        # response = requests.get(url)
        if response.status_code == 200: # status ok
            return response.text
        return None
    except RequestException:
        return None


def deal_real_page(html):
    pattern = re.compile('<p class="name">.*?title="([\s\S]*?)"[\s\S]*?data-act=[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>    </div>') #???
    results = re.findall(pattern, html)
    for item in results:
        yield{
           'title': item[0],
           'star': item[1],
           'releasetime': item[2]
        }

def write_file(content):
    with open("maoyan.txt", 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def get_top(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in deal_real_page(html):
        write_file(item)

if __name__ == '__main__':
    #线程也有池
    pool = Pool()
    pool.map(get_top, [i*10 for i in range(10)])
    pool.close()
    pool.join()

    print("over")

    # get_one_page("http://maoyan.com/board/4?offset=0")