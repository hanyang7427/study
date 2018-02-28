import numpy as np
a = np.arange(1, 10).reshape(3, 3)
print(a)
b = a * 100
print(b)
c = np.vstack((a, b))
print(c)
d = np.hstack((a, b))
print(d)
e = np.dstack((a, b))
print(e)
a.resize(9,)
print(a)
b.resize(9,)
print(b)
#f = np.vstack((a, b))
f = np.row_stack((a, b))
print(f)
#g = np.hstack((a.reshape(-1, 1), b.reshape(-1, 1)))
g = np.column_stack((a, b))
print(g)
h, i = np.vsplit(c, 2)
print(h, i, sep='\n')
j, k = np.hsplit(d, 2)
print(j, k, sep='\n')
l, m = np.dsplit(e, 2)
print(l, m, sep='\n')
print(l.T[0].T, m.T[0].T, sep='\n')