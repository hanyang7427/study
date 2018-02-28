import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
	[0, 0, 3],
	[1, 1, 0],
	[0, 2, 1],
	[1, 0, 2]])
print(raw_samples)
code_tables = []
for colume in raw_samples.T:
	code_table = {}
	for value in colume:
		code_table[value] = None
	code_tables.append(code_table)
for code_table in code_tables:
	size = len(code_table)
	for one, key in enumerate(sorted(code_table.keys())):
		code_table[key] = np.zeros(shape=size, dtype=int)
		code_table[key][one] = 1
ohe_samples = []
for raw_sample in raw_samples:
	ohe_sample = np.array([], dtype=int)
	for colume, feature in enumerate(raw_sample):
		ohe_sample = np.hstack((ohe_sample,
			code_tables[colume][feature]))
	ohe_samples.append(ohe_sample)
ohe_samples = np.array(ohe_samples)
print(ohe_samples)
ohe = sp.OneHotEncoder(sparse=False, dtype=int)
ohe_samples = ohe.fit_transform(raw_samples)
print(ohe_samples)
new_sample = np.array([[0, 2, 3]])
ohe_sample = ohe.transform(new_sample)
print(ohe_sample)
