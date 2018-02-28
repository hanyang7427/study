import numpy as np
a = np.array([
	[1+1j, 2+4j, 3+7j],
	[4+2j, 5+5j, 6+8j],
	[7+3j, 8+6j, 9+9j]])
print(a)
print(a.dtype)
print(a.shape)
print(a.T)
print(a.ndim)
print(a.size, len(a))
print(a.itemsize)
print(a.nbytes)
print(a.real)
print(a.imag)
print(list(a.flat))
# b = a.astype(np.str_)
b = a.astype(str)
print(b)
c = a.tolist()
print(c)
d = np.array(c)
print(d)