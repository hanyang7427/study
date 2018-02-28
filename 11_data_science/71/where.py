import numpy as np
a = np.array([1, 10, 3, 20, 5, 30, 7, 40, 9])
print(a)
b = a >= 10
print(b)
#c = np.where(b)
c = np.where(a >= 10)
print(c)
print(a[c])
print(a[np.where(a%2!=0)])
print(np.take(a, np.where(a%2!=0))[0])
a[np.where(a>=10)] += 1
print(a)
a[a>=10] += 1
print(a)