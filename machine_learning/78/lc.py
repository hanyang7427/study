import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp
data = []
with open('car.txt', 'r') as f:
	for line in f.readlines():
		data.append(line[:-1].split(','))
data = np.array(data).T
encoders, x = [], []
for row in range(len(data)):
	encoder = sp.LabelEncoder()
	if row < len(data) - 1:
		x.append(encoder.fit_transform(data[row]))
	else:
		y = encoder.fit_transform(data[row])
	encoders.append(encoder)
x = np.array(x).T
model = se.RandomForestClassifier(max_depth=8,
	n_estimators=200, random_state=7)
train_sizes = np.linspace(100, 1000, 10).astype(int)
train_sizes, tain_scores, test_scores = ms.learning_curve(
	model, x, y, train_sizes=train_sizes, cv=5)
print(train_sizes)
print(tain_scores.mean(axis=1))
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Learning Curve', fontsize=20)
mp.xlabel('Train Size', fontsize=14)
mp.ylabel('Score', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(100))
ax.yaxis.set_major_locator(mp.MultipleLocator())
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_sizes, tain_scores.mean(axis=1) * 100,
	'o-', c='dodgerblue', label='Learning Curve')
mp.legend()
mp.show()
