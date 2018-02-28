import functools
def f1(x, y):
	return x + y
a = [1, 2, 3]
print(a)
b = functools.reduce(f1, a)
print(b)
c = functools.reduce(lambda x, y: x + y, a)
print(c)
