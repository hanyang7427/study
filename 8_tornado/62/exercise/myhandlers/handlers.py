from io import BytesIO

import pymysql
from os.path import exists
# 此处红色没有错误
from utils.dbutil import DBUtil
from utils.md5 import md5
from utils.session import Session
from utils.imageutil import VertifyCode
from os import remove
import time
from tornado.web import RequestHandler

class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        s = Session(self)
        result = s['isLogin']
        if result:
            self.write('blog page')
        else:
            self.redirect('/')
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 往客户端写入cookie
        self.set_cookie('mycookie1', 'hello_cookie1')   # 没有expires_days，关闭浏览器cookie就没了
        self.set_cookie('mycookie2', 'hello_cookie2', expires_days=10)  # 10天
        s = Session(self)
        result = s['isLogin']
        if result:
            self.redirect('/blog')
        else:
            self.redirect('/loginpage')

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        try:
            username = self.get_query_argument('username')
            password = self.get_query_argument('password')
        except Exception as e:
            print(e,'aaaaaaa')
        dbutil = self.application.db    # RequestHandler实例的application
        pwd = md5(password)
        result = dbutil.isLoginSuccess(username, pwd)
        print('sss',result)
        if result:  # True用户名密码正确　False用户名密码不正确
            s = Session(self)
            s['isLogin'] = True
            self.redirect('/blog')
        else:
            self.redirect('/login')

class LoginPageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')


class RegisterHander(RequestHandler):
    def get(self, *args, **kwargs):
        mycookie = self.get_cookie('mycookie1')
        print('浏览器提交上的cookie:', mycookie)
        self.render('register.html')
    def post(self, *args, **kwargs):
        #1 获取客户端提交的内容
        name = self.get_argument('username')
        password = self.get_argument('password')
        city = self.get_argument('city')
        avatar = self.request.files.get('avatar',None)
        #2 判断内容的有效性(判空)
        if name and password and city:
            #3 处理头像图片，获得存储头像图片的名称
            avatar_file = None #头像图片存储的名称
            if avatar:
                file = avatar[0]       #httpFile对象
                avatar_file = str(time.time()) + file.filename
                avatar_body = file.body
                writer = open('mystatic/images/{}'.format(avatar_file),'wb')
                writer.write(avatar_body)
                writer.close()

            # 4　写入数据库
            pwd = md5(password)
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
                dbutil = DBUtil()
                params = dict(name=name,password=pwd,city=city,avatar_file=avatar_file)
                dbutil.saveuser(**params)
                self.redirect('/')
            #5 处理错误
            except Exception as e:
                print(e)
                #(1062, "Duplicate entry 'abc' for key 'user_name'")
                if avatar_file:
                    if exists('mystatic/images/'+avatar_file):
                        remove('mystatics/images/'+avatar_file)
                self.redirect('/register?regsit=dberror&error=dbfail')
        else:
            self.redirect('/register?regist=fail&error=reinput')


class CheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('get')
    def post(self, *args, **kwargs):
        ajax_type = self.get_argument('type')
        if ajax_type == 'emptyname':
            name = self.get_argument('username')
            print('ajax发送的用户名:', name)
            db = self.application.db
            if db.userNameExist(name):
                # 能用
                result = dict(msg='fail')
                self.write(result)
            else:
                # 不能用
                result = dict(msg='ok')
                self.write(result)
        if ajax_type == 'checkavatar':
            name = self.get_argument('loginname')
            db = self.application.db
            result = db.checkAvatar(name)
            if result:
                self.write(dict(msg=result))
            else:
                self.write(dict(msg='default'))
        if ajax_type == 'check_password_length':
            password = self.get_argument('password')
            print(password)
            # 注册时的密码长度限制，3位以上(不包含3位)
            password_len = 3
            if len(password)<=password_len:
                result = {'msg':'fail','password_len':password_len}
            else:
                result = {'msg':'ok'}
            self.write(result)
class CodeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        img,code = VertifyCode().create_pic()
        s = Session(self)
        s['code'] = code
        # 将图片存在流里，格式是jpeg
        io = BytesIO()
        img.save(io,'jpeg')
        img.close()
        self.set_header('Content-ajax_type','image/jpeg')
        self.write(io.getvalue())

    def post(self, *args, **kwargs):
        self.write('post')