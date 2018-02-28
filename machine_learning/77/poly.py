import numpy as np
import sklearn.pipeline as si
import sklearn.preprocessing as sp
import sklearn.linear_model as sl
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x, y = [], []
with open('single.txt', 'r') as f:
	for line in f.readlines():
		data = [float(substr) for substr in line.split(',')]
		x.append(data[:-1])
		y.append(data[-1])
x = np.array(x)
y = np.array(y)
train_size = int(x.size * 0.8)
train_x = x[:train_size]
train_y = y[:train_size]
model = si.make_pipeline(sp.PolynomialFeatures(7),
	sl.LinearRegression())
model.fit(train_x, train_y)
pred_train_y = model.predict(train_x)
test_x = x[train_size:]
test_y = y[train_size:]
pred_test_y = model.predict(test_x)
r2s = sm.r2_score(test_y, pred_test_y)
print(round(r2s, 2))
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Polynoimal Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_x, train_y, 's', c='limegreen', label='Training')
mp.plot(test_x, test_y, 's', c='orangered', label='Testing')
sorted_indices = train_x.T[0].argsort()
mp.plot(train_x.T[0][sorted_indices],
	pred_train_y[sorted_indices], c='dodgerblue',
	label='Predicted Training')
mp.legend()
mp.show()
