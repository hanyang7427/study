import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp
x, y = [], []
with open('multiple.txt', 'r') as f:
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
model = nb.GaussianNB()
model.fit(train_x, train_y)
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_test_y = model.predict(test_x)
ac = (pred_test_y == test_y).sum() / pred_test_y.size
print(ac)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator())
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.5))
ax.yaxis.set_major_locator(mp.MultipleLocator())
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.5))
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='brg')
mp.xlim(grid_x[0].min(), grid_x[0].max())
mp.ylim(grid_x[1].min(), grid_x[1].max())
mp.scatter(train_x[:, 0], train_x[:, 1], c=train_y,
	cmap='RdYlBu', s=80)
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y,
	cmap='RdYlBu', s=80, marker='D')
mp.scatter(test_x[:, 0], test_x[:, 1], c=pred_test_y,
	cmap='RdYlBu', s=80, marker='x')
mp.show()
