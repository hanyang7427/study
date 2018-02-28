# 5332
# tcpserver 第 [五] 步开始send或recv
##############################################
from socket import *
tss = socket(AF_INET,SOCK_STREAM)
tss.bind(('',8080))
tss.listen()                    # 此时可以连了
conn = tss.accept()             # 返回tuple，代表连接的conn和对方的地址
conn[0].send(''.encode())          # 返回发送的bytes个数，默认utf-8编码
conn[0].recv(1024).decode()        # 返回接收的数据，没有数据阻塞
                                # 如果对端close()，返回空bytes b''
conn[0].close()                    # 关闭连接socket
tss.close()                     # 关闭监听socket
##################################################
# tcpclient 第 [三] 步开始send或recv
from socket import *
tcs = socket(AF_INET,SOCK_STREAM)
tcs.connect(('localhost',8080))
tcs.send(''.encode())           # 返回发送的bytes个数，默认utf-8编码
tcs.recv(1024).decode()         # 返回接收的数据，没有数据阻塞
#####################################################
# udp server 第 [三] 步开始recv
from socket import *
uss = socket(AF_INET,SOCK_DGRAM)
uss.bind(('',9090))             # 此时可以连了
uss.recvfrom(1024)[0].decode()  # recvfrom返回tuple，0是data(bytes类型),1是地址和端口(tupel类型)
uss.sendto('data'.encode(),('localhost',9090))  # server端使用uss也可以发送数据，发送使用的端口是开放的端口
uss.close()
######################################################
# udp client 第 [二] 部开始send
from socket import *
ucs = socket(AF_INET,SOCK_DGRAM)
ucs.sendto('data'.encode(),('localhost',9090))  # 格式sendto(data,pair)
ucs.close()
