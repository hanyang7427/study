import functools
def f1(x):
	return x + 3
def f2(x):
	return x * 6
def f3(x):
	return x - 9
a = 1
print(a)
b = (a + 3) * 6 - 9
print(b)
c = f3(f2(f1(a)))
print(c)
fc = functools.reduce(
	lambda fa, fb: lambda x: fa(fb(x)), [f3, f2, f1])
d = fc(a)
print(d)
