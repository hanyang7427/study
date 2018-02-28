import random
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('indexpage')

    def post(self, *args, **kwargs):
        self.write('hello post')

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):

        name = self.get_argument('name')
        password = self.get_argument('password')

        print('name: ',name,'password',password)

        if name == 'abc' and password == '123':
            self.redirect('/blog')
        else:
            self.redirect('/')

class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #self.write('my blog')
        self.render('blog.html')
    def post(self, *args, **kwargs):
        pass
class MyBlogModule(UIModule):
    def fn(self):
        return 100
    def render(self, *args, **kwargs):          # 该函数的返回值会替换html中的{%module blogmod()%}
        # 给mod/mod_blog.html传参，传的参数可以不用，但是html中的变量必须传
        return self.render_string('mod/mod_blog.html',p1=200,p2=500,random=random,myrand=self.fn,
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
                            'avatar': ''
                        },{
                            'title': 'python博客',
                            'tag': ['科技','情感'],
                            'author': '老冯',
                            'content': 'python的四门功课说学逗唱',
                            'count': 145,
                            'avatar':'a.jpg'
                        }])
define('port',type=int,default=8888,multiple=False,help='setting port')
parse_config_file('config')
app = Application([(r'/',IndexHandler),
                   (r'/blog',BlogHandler)],
                  template_path='templates',            # html查找路径
                  ui_modules={'blogmod':MyBlogModule},  # 供给{%module blogmod()%}使用
                  static_path='./mystatic')             # 静态文件位置，也可以写绝对路径
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()
