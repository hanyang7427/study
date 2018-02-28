import pymysql
# 此处红色没有错误
from utils.md5 import md5

class DBUtil():
    def __init__(self,**kwargs):

        host = kwargs.get('host','127.0.0.1')
        port = kwargs.get('port',3306)
        user = kwargs.get('user','root')
        password = kwargs.get('password','123456')
        database = kwargs.get('database','blogdb')
        charset = kwargs.get('charset','utf8')

        config = dict(host=host,port=port,user=user,password=password,database=database,charset=charset)

        connection = pymysql.connect(**config)
        if connection:
            self.cursor = connection.cursor()
        else:
            raise Exception('数据库连接参数错误')

    #把用户信息写入tb_user数据表
    def saveuser(self,**kwargs):
        name = kwargs.get('name',None)
        password = kwargs.get('password',None)
        city = kwargs.get('city',None)
        avatar = kwargs.get('avatar_file',None)
        if name and password and city:
            sql='insert into ' \
                'tb_user(user_name,user_password,user_city,user_avatar) ' \
                'values(%s,%s,%s,%s)'
            params=(name,password,city,avatar)
            try:
                self.cursor.execute(sql,params)
                self.cursor.connection.commit()
            except Exception as e:
                print(e)
                raise Exception('保存用户时出现错误')
        else:
            raise Exception('参数不完整')

    # 验证用户登录是否成功
    def isLoginSuccess(self,name,password):
        sql='select count(*) ' \
            'from tb_user ' \
            'where user_name=%s and user_password=%s'
        pwd = md5(password)
        params=(name,pwd)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()#(0,) (1,)
        if result[0]:
            return True
        else:
            return False
    # 判断username在tb_user中有没有
    def userNameExist(self,name):
        sql = 'select count(*) from tb_user where user_name = %s'
        params = (name,)
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()
        if result[0]:
            return True
        else:
            return False
    def checkAvatar(self, name):
        sql = 'select user_avatar from tb_user where user_name = %s'
        params = (name,)
        print(params)
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None