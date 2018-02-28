import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as mp
train_x, train_y = [], []
with open('knn.txt', 'r') as f:
	for line in f.readlines():
		data = [float(substr) for substr in line.split(',')]
		train_x.append(data[:-1])
		train_y.append(data[-1])
train_x = np.array(train_x)
train_y = np.array(train_y, dtype=int)
model = sn.KNeighborsClassifier(n_neighbors=10,
	weights='distance')
model.fit(train_x, train_y)
l, r, h = train_x[:, 0].min() - 1, \
	train_x[:, 0].max() + 1, 0.005
b, t, v = train_x[:, 1].min() - 1, \
	train_x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
test_x = np.array([
	[2.2, 6.2],
	[3.6, 1.8],
	[4.5, 3.6]])
pred_test_y = model.predict(test_x)
nn_indices = model.kneighbors(test_x)[1]
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('KNN Classifier', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='brg')
mp.xlim(grid_x[0].min(), grid_x[0].max())
mp.ylim(grid_x[1].min(), grid_x[1].max())
classes = np.unique(train_y)
classes.sort()
cs = mp.get_cmap('RdYlBu', len(classes))(classes)
mp.scatter(train_x[:, 0], train_x[:, 1],
	c=cs[train_y], s=80)
mp.scatter(test_x[:, 0], test_x[:, 1], marker='D',
	c=cs[pred_test_y], s=120)
for i, nn_index in enumerate(nn_indices):
	mp.scatter(train_x[nn_index, 0], train_x[nn_index, 1],
		marker='D', edgecolor=cs[np.ones_like(
		nn_index) * pred_test_y[i]], facecolor='none',
		linewidth=2, s=180)
mp.show()
