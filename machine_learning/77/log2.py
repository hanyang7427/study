import numpy as np
import sklearn.linear_model as sl
import matplotlib.pyplot as mp
x = np.array([
	[4,   7  ],
	[3.5, 8  ],
	[3.1, 6.2],
	[0.5, 1  ],
	[1,   2  ],
	[1.2, 1.9],
	[6,   2  ],
	[5.7, 1.5],
	[5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
model = sl.LogisticRegression(solver='liblinear', C=100)
model.fit(x, y)
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Logistic Classification', fontsize=20)
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
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='RdYlBu', s=80)
mp.show()
