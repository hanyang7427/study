import hashlib
import uuid


def md5(password):
    m = hashlib.md5()
    m.update(password.encode('utf8'))
    return m.hexdigest()

#将ＵＵＩＤ值进行MD5
def getUUID():
    u = uuid.uuid4()
    print(u)
    m = hashlib.md5()
    m.update(u.bytes)
    return m.hexdigest()