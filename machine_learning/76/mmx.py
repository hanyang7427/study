import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
	[3, -1.5,  2,   -5.4],
	[0,  4,   -0.3,  2.1],
	[1,  3.3, -1.9, -4.3]])
print(raw_samples)
mmx_samples = raw_samples.copy()
cols = mmx_samples.shape[1]
for col in range(cols):
	col_samples = mmx_samples[:, col]
	col_min = col_samples.min()
	col_max = col_samples.max()
	k, b = np.linalg.lstsq(
		np.array([[col_min, 1], [col_max, 1]]),
		np.array([0, 1]))[0]
	col_samples *= k
	col_samples += b
print(mmx_samples)
mmx = sp.MinMaxScaler(feature_range=(0, 1))
mmx_samples = mmx.fit_transform(raw_samples)
print(mmx_samples)