import requests
headers={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Host":"www.cwl.gov.cn",
    "Referer":"http://www.cwl.gov.cn/kjxx/ssq/kjgg/",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=100'
response = requests.get(url,headers=headers)
print(response.text)