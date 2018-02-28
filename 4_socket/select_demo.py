from select import *
from socket import *
import sys
L = []
if __name__ == '__main__':
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(('',8081))
    sock.listen(5)
    L.append(sock)
    while True:
        readL,writeL,excrptL = select(L,[],[])
        for r in readL:
            if r == sock:
                conn,addr = r.accept()
                L.append(conn)
            else:
                data = r.recv(1024)
                if data:
                    print(data)
                else:
                    r.close()
                    L.remove(r)