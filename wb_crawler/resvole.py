import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs
import re
def resvole_http_raw(http_raw_req_file):
    re_header = re.compile(r'^([A-Z].*?): (.*)$')
    L = []
    def url2dict(url):
        query = urlparse(url).query
        return dict([(k, v[0]) for k, v in parse_qs(query).items()])
    with open(http_raw_req_file, 'r') as f:
        for line in f:
            L.append(line.strip())
    params_query = url2dict(L[0].split(' ')[1])
    params_body = dict([(k, v[0]) for k, v in parse_qs(L[-1]).items()])
    headers = []
    for header in L[1:-1]:
        if header:
            header = re.search(re_header, header).groups()
            headers.append(header)
    parmas_headers = dict(headers)
    return (params_query,params_body,parmas_headers)

def send_post_request(url, headers, data, params):
    content = requests.post(url, headers=headers, data=data, params=params).json()
    return content
def send_get_request(url, headers, params):
    content = requests.get(url, headers=headers, params=params).json()
    return content
    # 目标url
    # url = "https://weibo.com/aj/v6/comment/small"
    # with open('article_of_wan.csv','r',encoding='utf-8') as f1:
    #     for i in f1:
    #         params_query['mid'] = i.split(',')[1].split(' ')[1]
    #         params_query['sn'] = i.split(',')[1].split(' ')[2]
    #
    #         # 使用post方法进行提交
    #         content = requests.post(url, headers=parmas_headers, data=params_body, params=params_query).json()
    #         # 提取其中的阅读数和点赞数
    #         time.sleep(3)
    #         with open('result.csv', 'a', encoding='utf-8', newline='') as f2:
    #             writer = csv.writer(f2)
    # writer.writerow([i.split(',')[2].strip(), content["appmsgstat"]["read_num"], content["appmsgstat"]["like_num"]])
    #
    # ssl._create_default_https_context = ssl._create_unverified_context
    # target_url = "https://weibo.com/aj/v6/comment/small"
