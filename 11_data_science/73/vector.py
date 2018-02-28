import numpy as np
def fun(a, b, c):
	return a + b + c
x, y, z = 10, 20, 30
print(fun(x, y, z))
X = np.array([100, 200, 300])
Y = np.array([400, 500, 600])
Z = np.array([700, 800, 900])
R = np.vectorize(fun)(X, Y, Z)
print(R)
def max3(a, b, c):
	return np.array([a, b, c]).max()
print(max3(12, 33, 19))
print(max3(40, 20, 30))
A = np.array([10, 30, 70, 90, 20])
B = np.array([50, 40, 10, 90, 30])
C = np.array([20, 10, 50, 30, 40])
D = np.vectorize(max3)(A, B, C)
print(D)
