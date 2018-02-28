import numpy as np
a = np.arange(1, 7)
print(a)
b = a.reshape(2, 3)
print(a)
print(b)
b[0,0] += 10
print(a)
print(b)
#c = b.ravel()
c = b.flatten()
print(a)
print(b)
print(c)
c[0] += 10
print(a)
print(b)
print(c)
#c.shape=(3,2)
c.resize((3,2))
print(c)
#c.resize((6,))
c.shape=(6,)
print(c)
d = np.array([
	[1, 2],
	[3, 4],
	[5, 6]])
print(d)
#e = d.transpose()
e = d.T
print(e)
e[0][0] += 10
print(d)
print(e)
f = np.array([1,2,3])
print(f)
#g = f.T
g = f.reshape(-1, 1)
print(g)
h = g.T.ravel()
print(h)