import functools
import numpy as np
def f1(a):
	return map(lambda x: x + 3, a)
def f2(a):
	return map(lambda x: x * 6, a)
def f3(a):
	return map(lambda x: x - 9, a)
def function_composer(*fs):
	return functools.reduce(
		lambda fa, fb: lambda a: fa(fb(a)), fs)
a = np.array([1, 2, 3])
b = np.array(list(function_composer(f3, f2, f1)(a)))
print(b)