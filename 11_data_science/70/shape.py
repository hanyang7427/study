import numpy as np
a = np.arange(1, 6)
print(a)
b = np.arange(2, 11, 2)
print(b)
c = np.array([
	[1,  2,  3,  4],
	[5,  6,  7,  8],
	[9, 10, 11, 12],
	], dtype=float)
print(c)
d = np.array([
	np.arange(1, 5),
	np.arange(5, 9),
	np.arange(9, 13),
	])
print(d)
print(d[1][2])
print(d[1, 2])
print(type(d))
print(type(d[0]))
print(type(d[0][0]))
print(d.dtype)
print(d.shape)
e = d.astype(float)
print(e)
f = e.reshape((4, 3))
print(f)