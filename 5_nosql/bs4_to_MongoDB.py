'''
项目练习
访问烂番茄 https://www.rottentomatoes.com/critics/latest_reviews
下载最新影评信息，字段包括
    Rating(得分)
    Movie(电影名)
    Review(评论)
    Date(日期)
    Critic(评论者)
在mongodb创建一个数据库 Movies
在Movies库创建集合 Posts
把每一条影评编辑为一条文档
把文档插入到Posts集合中
提示：
import pymongo
from pymongo import MongoClient
from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
from pymongo import MongoClient
from urllib.request import urlopen
from bs4 import BeautifulSoup
# 生成mongodb客户端的一个对象
client = MongoClient()
# 创建一个叫movies的数据库
db = client.movies
# 把烂番茄网址打开并加载到一个变量html中
html = urlopen('https://www.rottentomatoes.com/critics/latest_reviews')
# 把html变量中的html文档解析，生成一个加obsobj的对象
bsobj = BeautifulSoup(html.read(),'lxml')
# 利用find函数查找bsobj中html标签为table，把搜索结果保存为一个叫table的变量中(提示查找条件可以用tables标签中的class属性，用字典表示法)
table = bsobj.find('table',{'class':'table table-striped verticalCenter'})
# 利用findAll函数查找table中的所有tr标签，保存的到一个叫rows的变量中
rows = table.findAll('tr')
'''
通过for循环，对row中的每一行row提取有用信息，利用findAll查找到每行中的所有td标签，获得td标签的文本信息,即表格中的数据。
将td对应的数据生成一条post文档，把汗rating,movie,review,data,critic。把post插入到集合posts中
提示
student = {name:'yang',age:'30',gender:'F'}
db.posts.insert_one(student)
'''
for tr in rows:
    L = []
    for td in tr.findAll('td'):
        L.append(td.get_text().strip())
    if L:
        post = {'rating':L[0],'movie':L[1],'review':L[2].split('\n')[0].strip(),
            'date':L[2].split('\n')[2].strip(),'critic':L[3].split('\n')[0].strip(),
            'source':L[3].split('\n')[2].strip()}
        db.posts.insert_one(post)
print('done')