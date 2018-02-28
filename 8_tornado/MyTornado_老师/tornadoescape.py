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


#ctrl + y
define('port',type=int,default=8888,multiple=False,help='setting port')
parse_config_file('config')
app = Application([(r'/',IndexHandler)],template_path='mytemplates',autoescape=None)
server = HTTPServer(app)
# 监听哪一个端口(最好>10000)
server.listen(options.port)
# 启动服务器
IOLoop.current().start()
