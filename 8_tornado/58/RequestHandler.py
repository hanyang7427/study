#tornadoresp练习服务器对客户端的响应
import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import RequestHandler, Application


# 执行顺序set_default_headers > initialize > get|post > on_finish > finish
class IndexHandler(RequestHandler):
    def set_default_headers(self):              # 继承自RequestHandler 固定写法，设置response的默认header
        self.set_header('myheader', 'mymymyheader')

    def initialize(self):                       # 继承自RequestHandler 固定写法，get和post之前执行
        pass

    def get(self, *args, **kwargs):             # 继承自RequestHandler 固定写法，处理get请求
        # 以下write写入到tornado的缓冲区,所以多行write都会输出到浏览器
        # self.write('<p>hello get1</p>')
        # self.write('<p>hello get2</p>')
        # self.write('<p>hello get3</p>')
        # 给浏览器返回字典
        # resp = dict(key1='value1', key2='value2')
        # self.write字典给浏览器时，response的header Content-Type自动设置为application/json
        # self.write(resp)

        # 手动设置响应头的Content-Type application/json;charset='UTF-8'
        self.set_header('Content-Type','application/json;charset=UTF-8')
        self.set_header('myheader','newheader')        # 覆盖set_default_headers中的set_header
        # 手动设定响应头的状态码
        # self.set_status(404)
        # self.set_status(888,'it is joke')            # 未知的status code 描述 必须写

        # 手动抛出错误，之前的代码不执行，开始进入write_error
        self.send_error()             # 返回http500，并调用write_error
        # self.send_error(200)        # 返回http200，但是是错误

        # send_error之后不能在写self.write
        # self.write('我会报错')

        def write_error(self, status_code, **kwargs):       # 注write_error会自动重新执行set_default_headers
            if status_code == 200:
                self.write('444:去死吧！')
            else:
                super().write_error(status_code,**kwargs)

    def post(self, *args, **kwargs):            # 继承自RequestHandler 固定写法，处理post请求
        self.write('hello post')

    def on_finish(self):                        # 继承自RequestHandler 固定写法，get和post之后执行
        print('on_finish方法获得了执行')
        # on_finish里不能用self.write
        # self.write('我会报错')

    # 继承自RequestHandler，不要重写此方法！！！
    # def finish(self, chunk=None):

define('port',type=int,default=8888,multiple=False,help='setting port')
parse_config_file('config')
app = Application([(r'/',IndexHandler)])
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()