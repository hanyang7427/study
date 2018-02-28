import numpy as np
a = np.array([
	[1, 1, 1, 1, 1, 1, 1],
	[1, 2, 2, 2, 2, 2, 1],
	[1, 2, 3, 3, 3, 2, 1],
	[1, 2, 3, 4, 3, 2, 1],
	[1, 2, 3, 3, 3, 2, 1],
	[1, 2, 2, 2, 2, 2, 1],
	[1, 1, 1, 1, 1, 1, 1]])
print(a)
b = a.clip(min=2, max=3)
print(b)
c = a.compress(a.ravel()>2).reshape(3, 3)
print(c)
d = a[a>2].reshape(3, 3)
print(d)
e = 1
for i in range(2, 6):
	e *= i
print(e)
f = np.arange(2, 6).prod()
print(f)
g = np.arange(2, 6).cumprod()
print(g)
