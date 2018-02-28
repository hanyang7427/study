import json
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler

class IndexHandler(RequestHandler):
    # 假如不传key1，会报错 400: Bad Request
    # 使用try解决
    # curl localhost:8000/?key1=1&key2=2&key2=3
    def get(self, *args, **kwargs):
        try:
            key1 = self.get_query_argument('key1')
        except Exception as e:
            print(e)
            key1 = 'Missing'
        key2s = self.get_query_arguments('key2')    # get_arg2s是一个列表
        self.write('key1:{}\nkey2s:{}'.format(key1,key2s))
    # curl -d 'key1=1&key2=2' localhost:8000/
    def post(self, *args, **kwargs):
        try:
            key1 = self.get_body_argument('key1')
        except Exception as e:
            print(e)
            key1 = 'Missing'
        key2s = self.get_body_arguments('key2')
        self.write('key1:{}\nkey2s:{}\n'.format(key1, key2s))
        print(1)
        # The Request.get_query_argument() looks for URL parameters 1st
        # the RequestHandler.get_body_argument() lets you retrieve parameters set in the POST body 2st
        # The RequestHandler.get_argument() method retrieves either a body or a URL parameter (in that order).
        # curl -d 'key2=2' 'localhost:8000/?key1=111&key2=222'
        try:
            all_key1 = self.get_argument('key1')
        except Exception as e:
            print(e)
            all_key1 = 'Missing'
        all_key2s=self.get_arguments('key2')
        self.write('all_key1:{}\nall_key2s:{}'.format(all_key1, all_key2s))

        # 获取用post方式发起请求的请求头中的内容
        # Content-Type: application/x-www-form-urlencoded
        # curl -H 'aa:aa' -d 'key1=1' localhost:8000/
        headers = self.request.headers      # 获得头部
        print(headers)
        print(headers.get('aa','aa missing'))

        # 处理浏览器发送的json格式的参数
        # curl -H "Content-Type:application/json" -X POST -d '{"1":1,"2":2}' localhost:8000
        # json 的key必须用双引号引起来(单引号不行)
        ct = headers.get('Content-Type')
        if ct == 'application/json':
            # 获取二进制格式的json字符串
            jsonStr = self.request.body
            # 二进制格式的字符串转成一个字符串
            str = jsonStr.decode('utf-8')
            # 利用json库将字符串转为json对象
            jsonObj = json.loads(str)
            # 利用json提供的API从json对象中取出我需要的内容
            for k,v in jsonObj.items():
                print(k,' = ',v)

        # 处理用户上传图片
        # curl -F "file1=@a" -F "file1=@b" -F "@file2=c.txt" localhost:8000/
        if ct.startswith('multipart/form-data'):
            print('用户上传了文件！')
            # upfiles为一个字典 {'file1':[{...},{...}],'file2':[{...}]}
            # 字典的内容：
            # content_type':'application/octet-stream'      # 上传文件的类型
            # 'body': b'aaaa\n'                             # 上传文件的字节码
            # 'filename': 'file2'                           # 上传的文件名
            upfiles = self.request.files
            for i in upfiles.get('file1'):
                filename = i.get('filename')
                with open('upload/{}'.format(filename),'wb') as file:
                    file.write(i.get('body'))


define('port',type=int,default=8000,multiple=False,help='setting port')
parse_config_file('config')
app = Application([(r'/',IndexHandler)])
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()