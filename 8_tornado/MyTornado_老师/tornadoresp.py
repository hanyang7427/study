#tornadoresp练习服务器对客户端的响应
import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import RequestHandler, Application

class IndexHandler(RequestHandler):
    def set_default_headers(self):
        print('set_default_header执行')
        self.set_header('myheader','mymymyheader')


    def get(self, *args, **kwargs):
        print('get方法获得了执行')
        # self.write('<p>hello get1</p>')
        # self.write('<p>hello get2</p>')
        # self.write('<p>hello get3</p>')
        # self.write('<p>hello get4</p>')
        # self.write('<p>hello get5</p>')
        # self.write('<p>hello get6</p>')
        # self.write('<p>hello get7</p>')

        #以下代码关于服务器以ｊｓｏｎ字符串形式进行响应
        #{'k':v}
        # 1 创建字典
        resp = dict(key1='value1',key2='value2')
        # 2 字典转成json字符串
        jsonstr = json.dumps(resp)
        # 3 利用self．write输出到浏览器
        self.write(jsonstr)
        # 4* 手动设置响应头的Content-Type application/json;charset='UTF-8'
        self.set_header('Content-Type','application/json;charset=UTF-8')
        self.set_header('myheader','newheader')
        #　手动设定状态码
        #self.set_status(888,'joke')

        # 手动抛出错误
        self.send_error(200)
        #!!!!注意，不能在send_error后面再有输出的代码
        #self.write(jsonstr)

        #self.write(resp)

    def write_error(self, status_code, **kwargs):
        if status_code == 200:
            self.write('<span style="color:red;font-weight:bold;font-size:36px">444:去死吧！</span>')
        else:
            super().write_error(status_code,**kwargs)

    def post(self, *args, **kwargs):
        self.write('hello post')

    def on_finish(self):
        print('on_finish方法获得了执行')

    def initialize(self):
        print('initialize方法获得执行')



define('port',type=int,default=8888,multiple=False,help='setting port')
parse_config_file('config')
app = Application([(r'/',IndexHandler)])
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()


