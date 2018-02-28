import time
from io import BytesIO
from os.path import exists
from os import remove
from tornado.web import RequestHandler

from util.imageutil import VertifyCode
from util.md5 import md5
from util.mysession import Session


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #往客户端写入ｃｏｏｋｉｅ
        self.set_cookie('mycookie','hello_cookie',expires_days=10)
        self.set_cookie('mycookie2','hello_cookie2',expires_days=10)
        self.set_cookie('mycookie3','hello_cookie3',expires_days=10)
        self.set_cookie('mycookie4','hello_cookie4',expires_days=10)
        #测试一下ｓｅｓｓｉｏｎ
        # s = Session(self)
        # s['islogin'] = False
        s = Session(self)
        result = s['islogin']
        if result:
            self.redirect("/blog")
        else:
            self.render('login.html')




    def post(self, *args, **kwargs):
        self.write('hello post')

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):

        name = self.get_argument('name')
        password = self.get_argument('password')


        dbutil = self.application.db

        result = dbutil.isLoginSuccess(name,password)

        if result:#True 用户名密码正确　False用户名密码不正确

            s = Session(self)
            s['islogin'] = True
            self.redirect('/blog')
        else:
            self.redirect('/?login=fail')

class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        mycookie = self.get_cookie('mycookie')
        print('浏览器提交上的ｃｏｏｋｉｅ:',mycookie)
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

        s = Session(self)
        result = s['islogin']
        if result:
            self.render('blog.html')
        else:
            self.redirect("/")

    def post(self, *args, **kwargs):
        pass

class CodeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #img是画着验证码的图片
        #ｃｏｄｅ字符串形式的验证码
        img,code = VertifyCode().create_pic()

        s = Session(self)
        s['code'] = code

        io= BytesIO()
        img.save(io,'jpeg')
        img.close()
        self.set_header('Content-Type','image/jpeg')
        self.write(io.getvalue())


    def post(self, *args, **kwargs):
        pass

class CheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("get")
    def post(self, *args, **kwargs):

        type = self.get_argument('type')

        if type=='emptyname':

            name = self.get_argument('username')
            print('ajax发送的用户名:',name)

            db = self.application.db
            if db.emptyName(name):
                #能用
                result = dict(msg='ok')
                self.write(result)
            else:
                #不能用
                result = dict(msg='fail')
                self.write(result)
        if type == 'checkavatar':
            name = self.get_argument('loginname')
            print('登录用户名：',name)
            db = self.application.db
            result = db.checkAvatar(name)
            print(result)
            if result[0]:
                self.write(dict(msg=result))
            else:
                self.write(dict(msg='default'))