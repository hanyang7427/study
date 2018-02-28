from utils.md5 import getUUID

# {xx1:{isLogin:True,name:'tom'}}
# {xx2:{isLogin:False,name:'jerry'}}
session={}
class Session():
    def __init__(self,handler):
        self.handler = handler

    def __getitem__(self, key):
        # s = Session()
        # s['islogin']
        cookieid = self.handler.get_cookie('cookieid')
        if cookieid:
            info = session.get(cookieid, None)
            if info:
                return info.get(key, None)
            else:
                return None
        else:
            return None

    def __setitem__(self, key, value):
        # s = Session()
        # s['key'] = value
        cookieid = self.handler.get_cookie('cookieid')
        if cookieid:
            info = session.get(cookieid, None)
            if info:
                info[key] = value
            else:
                d = dict()
                d[key] = value
                session[cookieid] = d
        else:
            d = dict()
            d[key] = value
            cookieid = getUUID()
            self.handler.set_cookie('cookieid', cookieid,expires_days=1)
            session[cookieid] = d