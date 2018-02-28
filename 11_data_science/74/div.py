import numpy as np
a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print(a, b)
c = np.true_divide(a, b)
d = np.divide(a, b)
e = a / b
print(c, d, e)
f = np.floor_divide(a, b)
g = a // b
print(f, g)
h = np.ceil(a / b).astype(int)
print(h)
i = np.trunc(a / b).astype(int)
j = (a / b).astype(int)
print(i, j)
k = np.remainder(a, b)
l = np.mod(a, b)
m = a % b
print(k, l, m)
n = np.fmod(a, b)
print(n)
