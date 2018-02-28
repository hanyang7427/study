import numpy as np
a = np.array([
	[9, 7, 5],
	[3, 1, 8],
	[6, 6, 1]])
print(np.max(a), np.min(a))
b = np.array([
	[6, 1, 9],
	[7, 1, 7],
	[4, 4, 5]])
print(np.maximum(a, b), np.minimum(a, b), sep='\n')
