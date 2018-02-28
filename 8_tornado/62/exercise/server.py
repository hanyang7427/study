from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from app.myapp import MyApplication
from myhandlers.handlers import IndexHandler,LoginHandler,LoginPageHandler,RegisterHander,CheckHandler,BlogHandler,CodeHandler
from mymodules.modules import MyloginModule,MyRegisterModule
from myconfig import myconfig

app = MyApplication([(r'/',IndexHandler),
                   (r'/login',LoginHandler),        # 直接在浏览器访问次url无意义
                   (r'/loginpage',LoginPageHandler),
                   (r'/register',RegisterHander),
                     (r'/check',CheckHandler),
                     (r'/blog',BlogHandler),
                     (r'/code',CodeHandler)],
                     {'loginmod': MyloginModule, 'registermod': MyRegisterModule},
                    'templates',
                    'mystatic')
server = HTTPServer(app)
server.listen(myconfig.configs.get('port',8888))
IOLoop.current().start()

