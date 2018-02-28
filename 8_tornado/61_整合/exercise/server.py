from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from app.myapp import MyApplication
from myhandlers.handlers import IndexHandler,UserHandler,LoginPageHandler,RegisterHander,CheckHandler
from mymodules.modules import MyloginModule,MyRegisterModule
from myconfig import myconfig

app = MyApplication([(r'/',IndexHandler),
                   (r'/login',UserHandler),
                   (r'/loginpage',LoginPageHandler),
                   (r'/register',RegisterHander),
                     (r'/check',CheckHandler)],
                     {'loginmod': MyloginModule, 'registermod': MyRegisterModule},
                    'templates',
                    './mystatic')
server = HTTPServer(app)
server.listen(myconfig.configs.get('port',8888))
IOLoop.current().start()

