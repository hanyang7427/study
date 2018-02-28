import numpy as np
def fibo_recursion(n):
	return 1 if n < 3 else fibo_recursion(n - 2) + \
		fibo_recursion(n - 1)
def fibo_loop(n):
	fn_2, fn_1 = 1, 0
	for i in range(n):
		fn = fn_2 + fn_1
		fn_2, fn_1 = fn_1, fn
	return fn
def fibo_matrix(n):
	return (np.mat('1. 1.; 1. 0.') ** (n - 1))[0, 0]
def fibo_binet(n):
	V5 = np.sqrt(5)
	return (((1+V5)/2)**n - ((1-V5)/2)**n) / V5
#print(fibo_recursion(40))
#print(fibo_loop(100))
#print(fibo_matrix(100))
print(fibo_binet(100))
