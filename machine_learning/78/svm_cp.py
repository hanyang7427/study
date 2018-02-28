import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x, y = [], []
with open('svm.txt', 'r') as f:
	for line in f.readlines():
		data = [float(substr) for substr in line.split(',')]
		x.append(data[:-1])
		y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
train_x, test_x, train_y, test_y = ms.train_test_split(
	x, y, test_size=0.25, random_state=5)
model = svm.SVC(kernel='rbf', C=600, gamma = 0.01,
	probability=True)
model.fit(train_x, train_y)
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_train_y = model.predict(train_x)
print(sm.classification_report(train_y, pred_train_y))
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))
cp_x = np.array([
	[2, 1.5],
	[8, 9],
	[4.8, 5.2],
	[4, 4],
	[2.5, 7],
	[7.6, 2],
	[5.4, 5.9]])
cp_y = model.predict(cp_x)
print(cp_y)
cp = model.predict_proba(cp_x)
print(cp)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('SVM RBF', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator())
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.5))
ax.yaxis.set_major_locator(mp.MultipleLocator())
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.5))
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.xlim(grid_x[0].min(), grid_x[0].max())
mp.ylim(grid_x[1].min(), grid_x[1].max())
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()
