from socket import *
from select import *
sock = socket(AF_INET,SOCK_STREAM)

# 设置套接字可以重复绑定
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sock.bind(('',8080))
sock.listen(5)
# 创建epoll对象
epoll = select.epoll()
# 注册事件file descript
# epoll.register(fd,[eventmask])
# 注意：如果这个fd已经注册过，再次注册会异常
epoll.register(sock.fileno(),EPOLLIN|EPOLLET)       # '|'表示并集

# 用来记录socket和客户端的地址
connections ={}
addresses = {}

while True:
    # poll()扫描
    epollList = epoll.poll()
    for fd in epollList:
        # 如果是监听socket
        if fd == sock.fileno():
            conn,addr = sock.accept()
            print("有新的客户连接%s"% str(addr))
            # 将服务socket的信息加入到字典中去
            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr
            # 服务socket的注册
            epoll.register(conn.fileno(),EPOLLIN|EPOLLET)
        # 入股服务socket
        elif fd.events == EPOLLIN:
            recvData =connections[fd].recv(1024)
            if len(recvData) > 0:
                print(recvData.decode('utf-8'))
            else:
                # 收不到数据则反注册epoll
                epoll.unregeister(fd)
                # 关闭socket
                connections[fd].close()
                print("%s 已经离开"% str(addresses[fd]))
