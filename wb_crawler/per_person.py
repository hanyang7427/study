import pickle
import resvole
import requests
import re
import csv
d = dict()
with open('users.plk','rb') as f:
    p = pickle.load(f)

new_p = []
for i in p:
    if i not in new_p:
        new_p.append(i)

http_raw_request_file = 'person_raw_request'
params = resvole.resvole_http_raw(http_raw_request_file)
cnt = 0
a = re.compile('<spanclass="item_textW_fl">(.*?)</span>')
b = re.compile('^weibo.com/(\d*)$')
with open('address.csv','w',encoding='utf-8') as f1:
    writer = csv.writer(f1)
    for i in new_p:
        print(i)
        cnt = cnt + 1
        print(cnt)
        try:
            num = re.search(b, i).groups()[0]
        except:
            num = 0
        if num:
            result = requests.get('https://weibo.com/u/'+num,headers=params[2])
            result = result.content.decode('utf-8')
            result = result.replace('\\t', '').replace('\\r', '').replace('\\n', '').replace(' ', '').replace('\\', '')
            address = re.findall(a,result)
        else:
            result = requests.get('https://'+i, headers=params[2])
            result = result.content.decode('utf-8')
            result = result.replace('\\t', '').replace('\\r', '').replace('\\n', '').replace(' ', '').replace('\\', '')
            address = re.findall(a, result)
        writer.writerow([i,address])