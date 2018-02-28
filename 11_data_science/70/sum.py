import datetime as dt
import numpy as np
n = 100000
start = dt.datetime.now()
a = [i ** 2 for i in range(n)]
b = [i ** 3 for i in range(n)]
c = []
for i in range(n):
	c.append(a[i] + b[i])
print((dt.datetime.now() - start).microseconds)
#print(a, b, c, sep='\n')
start = dt.datetime.now()
c = np.arange(n) ** 2 + np.arange(n) ** 3
print((dt.datetime.now() - start).microseconds)
#print(c)