from urllib.parse import urlparse
from urllib.parse import parse_qs
import re
re_header = re.compile(r'^([A-Z].*?): (.*)$')
L = []
def url2dict(url):
    query = urlparse(url).query
    return dict([(k, v[0]) for k, v in parse_qs(query).items()])
with open('request.txt', 'r') as f:
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

