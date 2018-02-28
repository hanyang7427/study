from tornado.web import Application

from myconfigs import myconfigs
from util.dbutil import DBUtil


class MyApplication(Application):
    def __init__(self, handlers, modules, tpath, spath):
        super().__init__(handlers=handlers,ui_modules=modules,template_path=tpath,static_path=spath)
        self.db = DBUtil(**myconfigs.configs.get('dbconfig'))