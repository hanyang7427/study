'''
抓取维基百科中，中国的城市
https://en.wikipedia.org/wiki/List_of_prefectures_in_the_People%27s_Republic_of_China
保存在csv文件中，包括
    Name
    Province
    Type
    Population
    Area
    Prefecture Seat
'''
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/List_of_prefectures_in_the_People%27s_Republic_of_China')
bsobj = BeautifulSoup(html.read(),'lxml')
table = bsobj.findAll('table',{'class':'wikitable sortable'})
rows = table[1].findAll('tr')
with open('city_of_china.csv','w') as csv_file:     # 写模式打开，覆盖原来文件
    writer = csv.writer(csv_file)
    for tr in rows:
        L = []
        for td in tr.findAll(['td','th']):
            L.append(td.get_text().replace(',',''))
        writer.writerow(L)