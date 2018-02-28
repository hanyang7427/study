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
model = se.RandomForestClassifier(max_depth=8, random_state=7)
n_estimators = np.linspace(20, 200, 20).astype(int)
tain_scores1, test_scores1 = ms.validation_curve(model, x, y,
	'n_estimators', n_estimators, cv = 5)
print(n_estimators)
print(tain_scores1.mean(axis=1))
model = se.RandomForestClassifier(n_estimators=200,
	random_state=7)
max_depth = np.linspace(1, 10, 10).astype(int)
tain_scores2, test_scores2 = ms.validation_curve(model, x, y,
	'max_depth', max_depth, cv = 5)
print(max_depth)
print(tain_scores2.mean(axis=1))
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(121)
mp.title('n_estimators', fontsize=16)
mp.xlabel('n_estimators', fontsize=12)
mp.ylabel('Score', fontsize=12)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(40))
ax.yaxis.set_major_locator(mp.MultipleLocator(0.1))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(n_estimators, tain_scores1.mean(axis=1) * 100,
	'o-', c='dodgerblue', label='Validation Curve')
mp.legend()
mp.subplot(122)
mp.title('max_depth', fontsize=16)
mp.xlabel('max_depth', fontsize=12)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(2))
ax.yaxis.set_major_locator(mp.MultipleLocator(5))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(max_depth, tain_scores2.mean(axis=1) * 100,
	'o-', c='orangered', label='Validation Curve')
mp.legend()
mp.tight_layout()
mp.show()
