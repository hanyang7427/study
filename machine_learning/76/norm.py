import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
	[3, -1.5,  2,   -5.4],
	[0,  4,   -0.3,  2.1],
	[1,  3.3, -1.9, -4.3]])
print(raw_samples)
nor_samples = raw_samples.copy()
rows = raw_samples.shape[0]
for row in range(rows):
	row_samples = nor_samples[row]
	row_abs = abs(row_samples)
	row_abs_sum = row_abs.sum()
	row_samples /= row_abs_sum
print(nor_samples)
print(np.abs(nor_samples).sum(axis=1))
nor_samples = sp.normalize(raw_samples, norm='l1')
print(nor_samples)