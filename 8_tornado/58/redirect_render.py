from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler

define('port',type=int,default=8888,multiple=False,help='setting post')
parse_config_file('config')

counter =0
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
        try:
            a = self.get_query_argument('username')
            b = self.get_query_argument('password')
            if a == 'ss' and b == 'ss':
                self.redirect('/')
            else:
                self.redirect('/loginpage')              # redirect跳转
        except Exception as e:
            print(e)

class LoginPageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # html = "<form method=get action=/login>" \
        #        "用户：<input type=text name=name><br/>" \
        #        "密码：<input type=password name=password><br/>" \
        #        "<input type=submit value=登录><input type=reset value=重置>" \
        #        "</form>"
        # self.write(html)

        # 使用render
        self.render('login.html')     # html在templates中查找，Application中设置template_path

app = Application([(r'/',IndexHandler),
                   (r'/login',UserHandler),
                   (r'/loginpage',LoginPageHandler)
                ],template_path='templates')      # 与当前文件同层目录下的mytemplates目录
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()

