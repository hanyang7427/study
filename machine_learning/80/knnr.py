import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as mp
train_x = 10 * np.random.rand(100, 1) - 5
train_y = np.sinc(train_x).ravel()
train_y += 0.2 * (0.5 - np.random.rand(train_y.size))
model = sn.KNeighborsRegressor(n_neighbors=10,
	weights='distance')
model.fit(train_x, train_y)
test_x = np.linspace(-5, 5, 10000).reshape(-1, 1)
pred_test_y = model.predict(test_x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('KNN Regressor', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
sorted_indices = train_x.ravel().argsort()
mp.plot(train_x[sorted_indices], train_y[sorted_indices],
	c='dodgerblue', label='Training')
mp.plot(test_x, pred_test_y,
	c='orangered', label='Testing')
mp.legend()
mp.show()