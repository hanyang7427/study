#!/usr/local/bin/python3
import pdb
pdb.set_trace()
print("这是第一行输出")
print("这是第二行输出")
def f1(n):
    print("这是f1中n的值：",n)
    n += 1
    print("这是f1中修改后的n的值：",n)
print("这是第三行的输出")

# 调用f1
f1(1)
x = 100
y = 200
z = x + y
f1(x)
print("程序结束：",x,y,z)


