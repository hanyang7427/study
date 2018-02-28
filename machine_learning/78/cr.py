import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import mpl_toolkits.axes_grid1 as mg
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
pc = ms.cross_val_score(model, x, y, cv=10,
	scoring='precision_weighted')
print(round(pc.mean(), 2))
rc = ms.cross_val_score(model, x, y, cv=10,
	scoring='recall_weighted')
print(round(rc.mean(), 2))
f1 = ms.cross_val_score(model, x, y, cv=10,
	scoring='f1_weighted')
print(round(f1.mean(), 2))
ac = ms.cross_val_score(model, x, y, cv=10,
	scoring='accuracy')
print(round(ac.mean(), 2))
model.fit(train_x, train_y)
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_test_y = model.predict(test_x)
ac = (pred_test_y == test_y).sum() / pred_test_y.size
print(round(ac, 2))
cm = sm.confusion_matrix(test_y, pred_test_y)
print(cm)
cr = sm.classification_report(test_y, pred_test_y)
print(cr)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(121)
mp.title('Naive Bayes Classification', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
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
mp.subplot(122)
mp.title('Confusion Matrix', fontsize=16)
mp.xlabel('Predicted', fontsize=12)
mp.ylabel('True', fontsize=12)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator())
ax.yaxis.set_major_locator(mp.MultipleLocator())
mp.tick_params(labelsize=10)
im = mp.imshow(cm, interpolation='nearest', cmap='jet')
for row in range(cm.shape[0]):
	for col in range(cm.shape[1]):
		mp.text(col, row, str(cm[row, col]), color='orangered',
			fontsize=12, fontstyle='italic', ha='center',
			va='center')
dv = mg.make_axes_locatable(mp.gca())
ca = dv.append_axes('right', '6%', pad='3%')
cb = mp.colorbar(im, cax=ca)
cb.set_label('Number of Samples', fontsize=12)
mp.show()
