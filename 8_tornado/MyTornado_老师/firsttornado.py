# alt + enter
# 孙伟　bjsunwei@tedu.cn
# python web frame:tornado

#127.0.0.1:9999
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, url


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<a href="/java">hello java</a>')

    def post(self, *args, **kwargs):
        self.write('hello post')

class JavaHandler(RequestHandler):

    def initialize(self,say,info):

        self.say = say
        self.info = info

    def get(self,p1,p2, *args, **kwargs):
        print('p1: ',p1,'p2: ',p2)
        self.write(self.say + ': ' + self.info)
        self.write('<br><a href={}>to python</a>'.format(self.reverse_url('python_url')))
    def post(self, *args, **kwargs):
        self.write('Hello Java post')

class PythonHandler(RequestHandler):
    def initialize(self,say,info):
        self.say = say
        self.info = info
    def get(self, *args, **kwargs):
        self.write(self.say+': '+self.info)
    def post(self, *args, **kwargs):
        self.write('Hello Python post')

define('port',type=int,default=8888,multiple=False,help='setting port')
define('db',type=str,default=[],multiple=True,help='db settings')
parse_config_file('config')
#创建服务器程序
#参数：根据客户端的访问路径
#     告诉服务器程序如何响应该请求

# 127.0.0.1:9999/java/article/string
# (r'/java/article/string', xxxxHandler)
app = Application([(r'/',IndexHandler),
                   (r'/java/(\w+)/([0-9a-z]+)',JavaHandler,{'say':'你好','info':'夹娃'}),
                   url(r'/python',PythonHandler,{'say':'Hello','info':'dear python!'},name='python_url')])#50%
server = HTTPServer(app)
# 监听哪一个端口(最好>10000)
server.listen(options.port)
print(options.db)
# 启动服务器
IOLoop.current().start()
