import pickle
import re
import resvole
with open('mids.plk','rb') as f:
    d = pickle.load(f)

a = re.compile(r'<a target="_blank" href="//(weibo.com/[^=]*?)" usercard')
http_raw_request_file = 'http_raw_request.txt'
url = 'https://weibo.com/aj/v6/comment/small'

L = []
L2 = []
for i in d.values():
    for j in i:
        L.append(j)


def get_ids_in_comment(mid):
    params = resvole.resvole_http_raw(http_raw_request_file)
    params[0]['mid']=mid
    ids = resvole.send_get_request(url,params[2],params[0])
    return ids

def get_weibo_address(html):
    return re.findall(a,html)
counter = 0
for i in L:
    print(i)
    counter = counter + 1
    print(counter)
    html = get_ids_in_comment(i)['data']['html']
    L2.append(get_weibo_address(html))
L3 = []
for i in L2:
    for j in i:
        L3.append(j)
with open('users.plk','wb') as f:
    pickle.dump(L3,f)