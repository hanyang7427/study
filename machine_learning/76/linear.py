import pickle
import numpy as np
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
model = sl.LinearRegression()
model.fit(train_x, train_y)
pred_train_y = model.predict(train_x)
test_x = x[train_size:]
test_y = y[train_size:]
pred_test_y = model.predict(test_x)
mae = sm.mean_absolute_error(test_y, pred_test_y)
mse = sm.mean_squared_error(test_y, pred_test_y)
mde = sm.median_absolute_error(test_y, pred_test_y)
evs = sm.explained_variance_score(test_y, pred_test_y)
r2s = sm.r2_score(test_y, pred_test_y)
print(round(mae, 2))
print(round(mse, 2))
print(round(mde, 2))
print(round(evs, 2))
print(round(r2s, 2))
with open('linear.pkl', 'wb') as f:
	pickle.dump(model, f)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_x, train_y, 's', c='limegreen', label='Training')
mp.plot(test_x, test_y, 's', c='orangered', label='Testing')
mp.plot(train_x, pred_train_y, c='dodgerblue',
	label='Predicted Training')
mp.legend()
mp.show()
