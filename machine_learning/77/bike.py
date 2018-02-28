import csv
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import sklearn.preprocessing as sp
import matplotlib.pyplot as mp
with open('bike_day.csv', 'r') as f:
	reader = csv.reader(f)
	x_day, y_day = [], []
	for row in reader:
		x_day.append(row[2:13])
		y_day.append(row[-1])
	feature_names_day = np.array(x_day[0])
	x_day = np.array(x_day[1:], dtype=float)
	y_day = np.array(y_day[1:], dtype=float)
	x_day, y_day = su.shuffle(x_day, y_day, random_state=7)
train_size_day = int(len(x_day) * 0.9)
train_x_day = x_day[:train_size_day]
train_y_day = y_day[:train_size_day]
model_day = se.RandomForestRegressor(
	max_depth=10, n_estimators=1000, min_samples_split=2)
model_day.fit(train_x_day, train_y_day)
test_x_day = x_day[train_size_day:]
test_y_day = y_day[train_size_day:]
pred_test_y_day = model_day.predict(test_x_day)
r2s = sm.r2_score(test_y_day, pred_test_y_day)
print(r2s)
with open('bike_hour.csv', 'r') as f:
	reader = csv.reader(f)
	x_hour, y_hour = [], []
	for row in reader:
		x_hour.append(row[2:14])
		y_hour.append(row[-1])
	feature_names_hour = np.array(x_hour[0])
	x_hour = np.array(x_hour[1:], dtype=float)
	y_hour = np.array(y_hour[1:], dtype=float)
	x_hour, y_hour = su.shuffle(x_hour, y_hour, random_state=7)
train_size_hour = int(len(x_hour) * 0.9)
train_x_hour = x_hour[:train_size_hour]
train_y_hour = y_hour[:train_size_hour]
model_hour = se.RandomForestRegressor(
	max_depth=10, n_estimators=1000, min_samples_split=2)
model_hour.fit(train_x_hour, train_y_hour)
test_x_hour = x_hour[train_size_hour:]
test_y_hour = y_hour[train_size_hour:]
pred_test_y_hour = model_hour.predict(test_x_hour)
r2s = sm.r2_score(test_y_hour, pred_test_y_hour)
print(r2s)
feature_importance_day = sp.MinMaxScaler(
	feature_range=(0, 100)).fit_transform(
		model_day.feature_importances_.reshape(-1, 1)).ravel()
feature_importance_hour = sp.MinMaxScaler(
	feature_range=(0, 100)).fit_transform(
		model_hour.feature_importances_.reshape(-1, 1)).ravel()
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(211)
mp.title('By Day', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = np.flipud(feature_importance_day.argsort())
pos = np.arange(sorted_indices.size)
mp.bar(pos, feature_importance_day[sorted_indices],
	align='center', facecolor='deepskyblue',
	edgecolor='steelblue', label='Day')
mp.xticks(pos, feature_names_day[sorted_indices], rotation=30)
mp.legend()
mp.subplot(212)
mp.title('By Hour', fontsize=16)
mp.xlabel('Feature', fontsize=12)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = np.flipud(feature_importance_hour.argsort())
pos = np.arange(sorted_indices.size)
mp.bar(pos, feature_importance_hour[sorted_indices],
	align='center', facecolor='deepskyblue',
	edgecolor='steelblue', label='Hour')
mp.xticks(pos, feature_names_hour[sorted_indices], rotation=30)
mp.legend()
mp.tight_layout()
mp.show()










