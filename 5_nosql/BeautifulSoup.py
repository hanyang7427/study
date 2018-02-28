# http://pythonscraping.com/pages/page3.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://pythonscraping.com/pages/page3.html')
bsobj = BeautifulSoup(html.read(), 'lxml')
children_counter = 0
descendants_counter = 0
siblings_counter = 0
print(bsobj.body.table.prettify())
# 遍历文档树的子节点(children) 6个</tr>
for child in bsobj.find('table',{'id':'giftList'}).children:
    if child != '\n':
        print(child)
        children_counter += 1
# 遍历文档的子孙节点(descendants)
for descendants in bsobj.find('table', {'id':'giftList'}).descendants:
    if descendants != '\n':
        print(descendants)
        descendants_counter += 1
# 下一个兄弟节点(sibling) 不包含自己5个</tr>
# next_sibling表示下一个兄弟标签，next_siblings表示多个下一个兄弟标签(迭代器)
# previous_sibling
for sibling in bsobj.find('table',{'id':'giftList'}).tr.next_siblings:
    if sibling != '\n':
        print(sibling)
        siblings_counter += 1
print('children:',children_counter)
print('descendants:',descendants_counter)
print('siblings:',siblings_counter)

# 查找src='../img/gifts/img1.jpg'的img标签 的 父标签的前一个子节点 的 标签中的文本
print(bsobj.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
# 查找img的地址
image = bsobj.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})