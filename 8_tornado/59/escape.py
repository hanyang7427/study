#演示转义

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, url


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('escape.html',text='')

    def post(self, *args, **kwargs):
        text = self.get_argument('text')
        self.render('escape.html',text=text)

define('port',type=int,default=8000,multiple=False,help='setting port')
parse_config_file('config')
# 关闭整个页面的转义autoescape=None
# app = Application([(r'/',IndexHandler)],template_path='templates',autoescape=None)
app = Application([(r'/',IndexHandler)],template_path='templates')
server = HTTPServer(app)
# 监听哪一个端口(最好>10000)
server.listen(options.port)
# 启动服务器
IOLoop.current().start()
