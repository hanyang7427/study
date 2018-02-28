import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, url

# tornado的定义变量方式
define('port', type=int, default=8888, multiple=False, help='port setting')
define('db', type=str, default=[], multiple=True, help='db setting')
# 从文件读取配置
parse_config_file('config')

print(options.db)

# 创建服务器程序
# 参数：根据客户端的访问路径，告诉服务器程序如何相应该请求
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<a href="/java">get java<a>')   # html
        self.write('<br/>')         # 结果累加出现在页面
        self.write('hello get')     # 结果累加出现在页面

    def post(self, *args, **kwargs):
        self.write('hello post')

class JavaHandler(RequestHandler):
    def initialize(self, say='hello', info='java'):
        self.say = say
        self.info = info
    def get(self, *args, **kwargs):
        self.write(self.say + ':' + self.info)

    def post(self, *args, **kwargs):
        self.write('hello java post')

class PythonHandler(RequestHandler):
    def initialize(self, say, info):
        self.say = say
        self.info = info
    def get(self, p1, p2, *args, **kwargs):
        print('p1: ', p1, 'p2: ', p2)
        self.write(self.say + ': ' + self.info)
        # self.write('<a href="%s">get python<a>' % self.reverse_url('python_url'))         # 给html传数据
        self.write('<a href="{}">get python<a>'.format(self.reverse_url('python_url')))
    def post(self, *args, **kwargs):
            self.write('Hello Python post')

# 127.0.0.1:9999/java/article/string
# (r'/java/article/string', xxxxHandler)
app = Application([(r'/', IndexHandler),
                   (r'/java', JavaHandler, {'say': '你好', 'info': 'java'}),
                   (r'/java/(\w+)/([0-9a-z]+)',JavaHandler),
                   url(r'/python', PythonHandler, {'say': '你好', 'info': 'python'},name='python_url')
                ])
server = HTTPServer(app)

# 监听那个端口(最好>10000)
server.listen(options.port)

# 启动服务器
IOLoop.current().start()
