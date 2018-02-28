import numpy as np
a = np.arange(-5, 6)
print(a)
b = -a
print(b)
c = a^b
print(c)
d = a.__xor__(b)
print(d)
e = np.bitwise_xor(a, b)
print(e)
f = e < 0
print(f)
g=np.arange(1, 21)
print(g)
h=g-1
print(h)
i=g&h
print(i)
j=g.__and__(h)
print(j)
k=np.bitwise_and(g, h)
print(k)
print(g[k==0])
l=np.ones(5, dtype=int)
print(l)
m = l * 2
print(m)
n = np.arange(5)
print(n)
o = m ** n
print(o)
p = l << n
print(p)
q = l.__lshift__(n)
print(q)
r = np.left_shift(l, n)
print(r)