import numpy as np
x = np.array([20, 30, 20, 10, 30, 30, 20, 10, 30])
y = np.array([ 7,  2,  5,  1,  8,  9,  6,  4,  3])
a = np.lexsort ((y, x))
print(x[[a]])
print(y[[a]])
z = x + y * 1j
b = np.sort_complex(z)
print(b)