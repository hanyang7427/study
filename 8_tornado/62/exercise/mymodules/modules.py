from tornado.web import UIModule
class MyRegisterModule(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string('mod/mod_register.html')
class MyloginModule(UIModule):
    def render(self, *args, **kwargs):
        q = self.request.query
        if q:
            res = '用户名或密码错误'
            return self.render_string('mod/mod_login_code.html', result=res)
        else:
            return self.render_string('mod/mod_login_code.html', result='')
