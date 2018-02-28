def f1(x):
	return x + 3
a = [1, 2, 3]
print(a)
b = list(map(f1, a))
print(b)
c = list(map(lambda x: x + 3, b))
print(c)
