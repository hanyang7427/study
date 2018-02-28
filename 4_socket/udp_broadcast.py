from socket import *
uSock = socket(AF_INET,SOCK_DGRAM)
# 设置广播
uSock.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
# 发送广播
uSock.sendto("hello world1".encode('utf-8'),('<broadcast>',8082))

# arp -a |grep -i 'xx:xx'查看mac对应ip