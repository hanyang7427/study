import pymysql
from os.path import exists
# 此处红色没有错误
from utils.dbutil import DBUtil
from utils.md5 import md5
from os import remove
import time
from tornado.web import RequestHandler


class A():
    pass

counter=0
class IndexHandler(RequestHandler):
    def get(self):
        # if self.request.remote_ip == '172.60.20.136':
        # if self.request.remote_ip == '172.60.20.82':
        if self.request.remote_ip == '127.0.0.1':
            global counter
            counter +=1
            print(counter)
            if counter >= 5:
                self.send_error(500)
            else:
                self.write('index page')
        else:
            self.write('index page')

class UserHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # config = {
        #     'host':'127.0.0.1',
        #     'port':3306,
        #     'user':'root',
        #     'password':'123456',
        #     'database':'blogdb',
        #     'charset':'utf8',
        # }
        # connection = pymysql.connect(**config)
        # cursor = connection.cursor()
        try:
            username = self.get_query_argument('username')
            password = self.get_query_argument('password')
        #     pwd = md5(password)
        #     params = (username,pwd)
        #     sql = 'select count(*) from tb_user where user_name=%s and user_password=%s'
        #     cursor.execute(sql,params)
        #     result = cursor.fetchone()
        #     if result[0]:
        #         self.redirect('/')
        #     else:
        #         self.redirect('/loginpage?loginfail')
        except Exception as e:
            print(e)
        dbutil = self.application.db    # RequestHandler实例的application
        pwd = md5(password)
        result = dbutil.isLoginSuccess(username, pwd)

        if result:  # True 用户名密码正确　False用户名密码不正确
            self.redirect('/blog')
        else:
            self.redirect('/?login=fail')

class LoginPageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')



class RegisterHander(RequestHandler):
    def get(self, *args, **kwargs):
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
        type = self.get_argument('type')
        if type == 'emptyname':
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
        if type == 'checkavatar':
            name = self.get_argument('loginname')
            print('登录用户名：', name)
            db = self.application.db
            result = db.checkAvatar(name)
            print(result)
            if result:
                self.write(dict(msg=result))
            else:
                self.write(dict(msg='default'))
        if type == 'check_password_length':
            password = self.get_argument('password')
            print(password)
            # 注册时的密码长度限制，3位以上(不包含3位)
            password_len = 3
            if len(password)<=password_len:
                result = {'msg':'fail','password_len':password_len}
            else:
                result = {'msg':'ok'}
            self.write(result)
