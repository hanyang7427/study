#用来学习页面跳转，模板
import random

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, url, UIModule

from app.myapp import MyApplication
from myconfigs import myconfigs
from myhandlers.myhandlers import IndexHandler, LoginHandler, BlogHandler, RegistHandler, CheckHandler, CodeHandler
from mymodules.mymodules import MyBlogModule, MyLoginModule, MyRegistModule
from util.imageutil import VertifyCode

app = MyApplication(handlers = [(r'/',IndexHandler),
                   (r'/login',LoginHandler),
                   (r'/blog',BlogHandler),
                   (r'/regist',RegistHandler),
                    (r'/check',CheckHandler),
                                (r'/code',CodeHandler)],
                    modules ={'myblogmodule':MyBlogModule,'myloginmodule':MyLoginModule,'myregistmodule':MyRegistModule},
                    tpath = 'mytemplates',
                    spath = 'mystatics')
server = HTTPServer(app)
server.listen(myconfigs.configs.get('port',8888))
IOLoop.current().start()
