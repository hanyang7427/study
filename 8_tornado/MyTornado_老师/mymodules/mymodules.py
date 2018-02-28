from tornado.web import UIModule


class MyLoginModule(UIModule):
    def render(self, *args, **kwargs):
        res = ''
        #/ 第一次加载login.html
        #/?login=fail 用户名或密码错误
        #self.request.path,uri
        q = self.request.query
        if q:
            res='用户名或密码错误'
        return self.render_string('module/module_login_code.html',result=res)
class MyBlogModule(UIModule):
    def my(self):
        return 100
    def render(self, *args, **kwargs):
        return self.render_string('module/module_blog.html',myrand=self.my,
                    blogs=[
                    {
                     'title':'第一篇博客',
                     'tag':['情感','文艺','清新'],
                     'author':'王小五',
                     'content':'好多正文好多正文好多正文',
                     'count':45,
                     'avatar':'a.jpg'
                    },{
                            'title': '今天的博客',
                            'tag': ['情感', '重口味'],
                            'author': '王老五',
                            'content': '不知道写点啥，随便吧',
                            'count': 0,
                            'avatar':''
                        },{
                            'title': 'python博客',
                            'tag': ['科技','情感'],
                            'author': '老冯',
                            'content': 'python的四门功课说学逗唱',
                            'count': 145,
                            'avatar':'a.jpg'
                        }])
class MyRegistModule(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string('module/module_regist.html')