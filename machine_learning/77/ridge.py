import numpy as np
import sklearn.linear_model as sl
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x, y = [], []
with open('abnormal.txt', 'r') as f:
	for line in f.readlines():
		data = [float(substr) for substr in line.split(',')]
		x.append(data[:-1])
		y.append(data[-1])
x = np.array(x)
y = np.array(y)
train_size = int(x.size * 0.8)
train_x = x[:train_size]
train_y = y[:train_size]
model1 = sl.LinearRegression()
model1.fit(train_x, train_y)
model2 = sl.Ridge(150, fit_intercept=True, max_iter=10000)
model2.fit(train_x, train_y)
pred_train_y1 = model1.predict(train_x)
pred_train_y2 = model2.predict(train_x)
test_x = x[train_size:]
test_y = y[train_size:]
pred_test_y1 = model1.predict(test_x)
pred_test_y2 = model2.predict(test_x)
r2s = sm.r2_score(test_y, pred_test_y1)
print(round(r2s, 2))
r2s = sm.r2_score(test_y, pred_test_y2)
print(round(r2s, 2))
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Linear vs. Ridge', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_x, train_y, 's', c='limegreen', label='Training')
mp.plot(test_x, test_y, 's', c='orangered', label='Testing')
mp.plot(train_x, pred_train_y1, c='dodgerblue', label='Linear')
mp.plot(train_x, pred_train_y2, c='crimson', label='Ridge')
mp.legend()
mp.show()
