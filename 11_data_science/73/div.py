import numpy as np
# 真除
a = np.array([5,5,-5,-5])
b = np.array([2,-2,2,-2])
print(a,b)
c = np.true_divide(a,b)
d = np.divide(a,b)
e = a/b
print(c,d,e)
# 地板除(向下取整)
f = np.floor_divide(a,b)
g = a//b
print(f,g)
# 天花板除(向上取整)
h = np.ceil(a/b).astype(int)
print(h)
# 截断除
i = np.trunc(a/b).astype(int)
j = (a/b).astype(int)
print(i,j)
# 地板模
k = np.remainder(a,b)
l = np.mod(a,b)
m = a % b
# 截断模
print(k,l,m)
n = np.np.fmod(a,b)
print(n)