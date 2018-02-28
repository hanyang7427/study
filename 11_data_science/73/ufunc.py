import numpy as np
def func(a, b):
	c = a + b
	d = a - b
	e = a * b
	return c, d, e
print(func(1, 5))
A = np.array([1, 2, 3, 4, 5])
B = np.array([5, 4, 3, 2, 1])
ufunc = np.frompyfunc(func, 2, 3)
C, D, E = ufunc(A, B)
print(C, D, E, sep='\n')
def func1(a):
	def func2(b):
		return a + b
	return np.frompyfunc(func2, 1, 1)
f100 = func1(100) 
F = f100(A)
print(F)





