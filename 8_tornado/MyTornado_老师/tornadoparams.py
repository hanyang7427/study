import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):

    #127.0.0.1:9999?key1=%BD%AC%78%0F%FE&key2=value2

    def get(self, *args, **kwargs):
        try:
            arg1 = self.get_query_argument('key1')
            #arg2 = self.get_query_argument('key2')
            arg2s = self.get_query_arguments('key2')
        except Exception as e:
            arg1 = 'Missing'
            #arg2 = 'Missing'
        # Ctrl + D
        #print('arg1: ',arg1,'arg2: ',arg2,'arg2s: ',arg2s)
        print('arg1: ',arg1,'arg2s: ',arg2s)
        self.write('hello get')

    def post(self, *args, **kwargs):
        # try:
        #     arg1 = self.get_body_argument('key1')
        #     arg2s = self.get_body_arguments('key2')
        #
        #     a1 = self.get_argument('key1')
        #
        #     a2s = self.get_arguments('key2')
        #
        # except Exception as e:
        #     arg1 = 'Missing'
        # print('arg1: ', arg1, 'arg2s: ', arg2s)
        # print('a1: ',a1,'a2s:',a2s)


        #获取用ｐｏｓｔ方式发起请求的请求头中的内容
        headers = self.request.headers
        print(headers)

        myheader = headers['my_header']
        h = headers.get('hello')

        print('myheader:',myheader,'h:',h)

        #处理浏览器发送的ｊｓｏｎ格式的参数
        #获取请求头中Content-Type的值
        ct = headers.get('Content-Type')
        if ct == 'application/json':
            #获取二进制格式的ｊｓｏｎ字符串
            jsonStr = self.request.body
            #二进制格式的字符串转成一个字符串
            str = jsonStr.decode('utf-8')
            #利用ｊｓｏｎ库将字符串转为ｊｓｏｎ对象
            jsonObj = json.loads(str)
            #利用ｊｓｏｎ提供的ＡＰＩ从ｊｓｏｎ对象中
            #取出我需要的内容
            for k,v in jsonObj.items():
                print(k,' = ',v)

        #处理用户上传图片
        if ct.startswith('multipart/form-data'):
            print('用户上传了文件！')

            #1 获取用户上传的文件request.files
            #{'avatar':[httpfile1,httpfile2...]}
            files=self.request.files
            #2 获取'avatar'键所对应的值[httpfile1,httpfile2]
            avatars = files.get('avatar')
            #3 遍历所有的httpfile
            for avatar in avatars:
                #4 httpfile的ｆｉｌｅｎａｍｅ对应的是图片本身的名字
                #  httpfile['filename']或httpfile.get('filename')
                filename = avatar['filename']
                #  httpfile的ｂｏｄｙ属性对应的图片数据本身(二进制)
                #  httpfile['body']或者httpfile.get('body')
                body = avatar['body']
                #5 利用ＩＯ，将图片的二进制保存为一个文件到服务器
                writer = open('upload/{}'.format(filename),'wb')
                writer.write(body)
                writer.close()

        self.write('hello post')




define('port',type=int,default=8888,multiple=False,help='setting port')
parse_config_file('config')
app = Application([(r'/',IndexHandler)])
server = HTTPServer(app)
server.listen(options.port)
IOLoop.current().start()