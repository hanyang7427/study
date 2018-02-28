#session

#{xxxx1:{islogin:True,name:'tom'},
# xxxx2:{islogin:False,name:'jerry',gedner='female'},
# xxxx3:{islogin:True,name:'lucy'},
# xxxx4:{key,value},
# 1234567:{key,value},
#f80274eee6f29459ee1d8d8b9fd2214b:{islogin:False}}
from util.md5 import getUUID

session={}

class Session():
    def __init__(self,handler):
        self.handler = handler

    def __getitem__(self, key):#islogin
        # s = Session()
        # s['islogin']
        cookieid = self.handler.get_cookie('cookieid')
        if cookieid:
            info = session.get(cookieid,None)
            if info:
                return info.get(key,None)
            else: return None

        else: return None

    def __setitem__(self, key, value):#key = islogin, value=False
        # s = Session()
        # s['key'] = value
        cookieid = self.handler.get_cookie('cookieid')
        if cookieid:
            info = session.get(cookieid,None)
            if info:
                info[key] = value
            else:
                d = dict()
                d[key] = value
                session[cookieid] = d
        else:
            d = dict()
            d[key] = value #{"islogin":False}
            cookieid = getUUID() #f80274eee6f29459ee1d8d8b9fd2214b
            self.handler.set_cookie('cookieid',cookieid,expires_days=1)
            session[cookieid] = d
