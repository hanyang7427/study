import numpy as np
a = np.arange(1, 7)
print(a)
b = np.add.reduce(a)
print(b)
c = np.add.accumulate(a)
print(c)
d = np.add.reduceat(a, [0, 2, 4])
print(d)
e = np.arange(1, 4) * 10
print(e)
f = np.add.outer(e, a)
print(f)
g = np.add.outer(a, e)
print(g)
h = np.outer(a, e)
print(h)