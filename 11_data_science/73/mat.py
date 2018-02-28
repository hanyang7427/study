import numpy as np
a = np.arange(1, 10).reshape(3, 3)
print(a)
b = np.arange(1, 10)[::-1].reshape(3, 3)
print(b)
c = a * b
print(c)
d = np.matrix(a)
print(d)
e = np.matrix(b)
print(e)
f = d * e
print(f)
#g = np.array([10, 20, 30], dtype=float)
#g = np.matrix([10, 20, 30], dtype=float)
#g = np.matrix('10 20 30; 40 50 60; 70 80 90', dtype=float)
g = np.mat('10 20 30; 40 50 60; 70 80 90', dtype=float)
print(g)
h = g
h[0,0] = 0
print(h, g, sep='\n')
i = np.mat(g)
i[0,0] = -1
print(i, g, sep='\n')
j = np.matrix(g, copy=False)
j[0,0] = -2
print(j, g, sep='\n')
print(j.T)
print(j.I)
print(j * j.I)
k = np.ones(9).reshape(3, 3).astype(int)
print(k)
l = k * 2
print(l)
m = k * 3
print(m)
n = k * 4
print(n)
o = np.vstack((np.hstack((l, k)), np.hstack((m, n))))
print(o)
p = np.bmat('l k; m n')
print(p)
