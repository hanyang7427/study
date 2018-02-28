#用来学习页面跳转，模板
import random

from os.path import join, dirname, exists

import pymysql
import time

from os import remove
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, url, UIModule

from app.myapp import MyApplication
from util.dbutil import DBUtil
from util.md5 import md5

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # html="<form method=post action=/login>" \
        #      "用户名：<input type=text name=name><br>" \
        #      "密码：<input type=password name=password><br>" \
        #      "<input type=submit value=登录><input type=reset value=重置>" \
        #      "</form>"
        #
        # self.write(html)

        self.render('login.html')

    def post(self, *args, **kwargs):
        self.write('hello post')

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):

        name = self.get_argument('name')
        password = self.get_argument('password')

        # print('name: ',name,'password',password)
        #
        # #根据用户输入的用户名和密码
        # #利用pymysql到数据表中查询
        # #根据查询结果跳转界面
        # config={
        #     'host':'127.0.0.1',
        #     'port':3306,
        #     'user':'root',
        #     'password':'123456',
        #     'database':'blogdb',
        #     'charset':'utf8'
        # }
        # connection = pymysql.connect(**config)
        # cursor = connection.cursor()
        # sql='select count(*) ' \
        #     'from tb_user ' \
        #     'where user_name=%s ' \
        #     'and user_password=%s'
        #
        # pwd = md5(password)#对用户输入的password进行md5编码
        # params = (name,pwd)
        # print('sql语句：',sql)
        # cursor.execute(sql,params)
        # #result = cursor.fetchall()#((0,),)
        # result = cursor.fetchone()#(0,) (1,)
        #
        # print(result)

        dbutil = self.application.db

        result = dbutil.isLoginSuccess(name,password)

        if result:#True 用户名密码正确　False用户名密码不正确
            self.redirect('/blog')
        else:
            self.redirect('/?login=fail')

class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')
    def post(self, *args, **kwargs):
        #1 获取客户端提交的内容
        name = self.get_argument('name')
        password = self.get_argument('password')
        city = self.get_argument('city')
        avatar = self.request.files.get('avatar',None)
        #2 判断内容的有效性(判空)
        if name and password and city:
            #3 处理头像图片，获得存储头像图片的名称
            avatar_file = None #头像图片存储的名称
            if avatar:
                file = avatar[0];#httpFile对象
                avatar_file = str(time.time()) + file.filename
                avatar_body = file.body
                writer = open('mystatics/images/{}'.format(avatar_file),'wb')
                writer.write(avatar_body)
                writer.close()

            # 4　写入数据库
            pwd = md5(password)#对用户输入的ｐａｓｓｗｏｒｄ进行md5编码处理
            # params = (name,pwd,city,avatar_file)
            # config={
            #     'host':'127.0.0.1',
            #     'port':3306,
            #     'user':'root',
            #     'password':'123456',
            #     'database':'blogdb',
            #     'charset':'utf8'
            # }
            # try:
            #     connection = pymysql.connect(**config)
            #     cursor = connection.cursor()
            #     sql='insert into ' \
            #         'tb_user(user_name,user_password,user_city,user_avatar)' \
            #         ' values(%s,%s,%s,%s)'
            #     cursor.execute(sql,params)
            #     cursor.connection.commit()#提交修改
            #     self.redirect('/')
            try:
                dbutil = self.application.db
                params = dict(name=name,password=pwd,city=city,avatar_file=avatar_file)
                dbutil.saveuser(**params)
                self.redirect('/')
            #5 处理错误
            except Exception as e:
                print(e)
                #(1062, "Duplicate entry 'abc' for key 'user_name'")
                if avatar_file:
                    if exists('mystatics/images/'+avatar_file):
                        remove('mystatics/images/'+avatar_file)

                self.redirect('/regist?regsit=dberror&error=dbfail')
        else:
            self.redirect('/regist?regist=fail&error=reinput')



class BlogHandler(RequestHandler):

    def get(self, *args, **kwargs):
        #self.write('my blog')
        self.render('blog.html')
    def post(self, *args, **kwargs):
        pass
class MyLoginModule(UIModule):
    def render(self, *args, **kwargs):
        res = ''
        #/ 第一次加载login.html
        #/?login=fail 用户名或密码错误
        #self.request.path,uri
        q = self.request.query
        if q:
            res='用户名或密码错误'
        return self.render_string('module/module_login.html',result=res)
class MyBlogModule(UIModule):
    def my(self):
        return 100
    def render(self, *args, **kwargs):
        return self.render_string('module/module_blog.html',p=200,q=500,random=random,myrand=self.my,
                    blogs=[
                    {
                     'title':'第一篇博客',
                     'tag':['情感','文艺','清新'],
                     'author':'王小五',
                     'content':'好多正文好多正文好多正文',
                     'count':45,
                     'avatar':'a.jpg'
                    },{
                            'title': '今天的博客',
                            'tag': ['情感', '重口味'],
                            'author': '王老五',
                            'content': '不知道写点啥，随便吧',
                            'count': 0,
                            'avatar':''
                        },{
                            'title': 'python博客',
                            'tag': ['科技','情感'],
                            'author': '老冯',
                            'content': 'python的四门功课说学逗唱',
                            'count': 145,
                            'avatar':'a.jpg'
                        }])
class MyRegistModule(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string('module/module_regist.html')
define('port',type=int,default=8888,multiple=False,help='setting port')
parse_config_file('config')
app = MyApplication(handlers = [(r'/',IndexHandler),
                   (r'/login',LoginHandler),
                   (r'/blog',BlogHandler),
                   (r'/regist',RegistHandler)],
                    modules ={'myblogmodule':MyBlogModule,'myloginmodule':MyLoginModule,'myregistmodule':MyRegistModule},
                    tpath = 'mytemplates',
                    spath = 'mystatics')
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()
