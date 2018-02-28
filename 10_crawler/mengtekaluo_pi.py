# -*- coding:utf-8 -*-
import random
import math

# 利用蒙特卡洛算法求pi的值
def mengtekaluoCalPi():
    n = int(input("请输入迭代的次数:"))
    pointInNum = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2+y**2) < 1.0:
            pointInNum += 1
    return pointInNum*4.0/n

print(mengtekaluoCalPi())