import numpy as np
import sklearn.decomposition as dc
a = np.random.normal(size=250)
b = np.random.normal(size=250)
c = 2 * a + 3 * b
d = 4 * a - b
e = c + 2 * d
x = np.c_[d, b, e, a, c]
print(x)
model = dc.PCA()
model.fit(x)
variance = model.explained_variance_
print(variance)
threshols = 0.8
useful_indices = np.where(variance > 0.8)[0]
n_useful = len(useful_indices)
print(n_useful)
model.n_components = n_useful
x = model.fit_transform(x)
print(x)
