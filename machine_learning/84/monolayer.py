import numpy as np
import neurolab as nl
import matplotlib.pyplot as mp
data = np.loadtxt('monolayer.txt')
train_x, train_y = data[:, :2], data[:, 2:]
train_labels = []
for train_row in train_y:
	train_row = train_row.astype(int).astype(str)
	train_labels.append('.'.join(train_row))
label_set = np.unique(train_labels)
train_codes = []
for train_label in train_labels:
	train_code = np.where(label_set == train_label)[0][0]
	train_codes.append(train_code)
train_codes = np.array(train_codes)
model = nl.net.newp([[train_x[:, 0].min(), train_x[:, 0].max()],
	[train_x[:, 1].min(), train_x[:, 1].max()]], 2)
error = model.train(train_x, train_y, epochs=50, show=20, lr=0.01)
test_x = np.array([
	[0.3, 4.5],
	[4.5, 0.5],
	[4.3, 8.0],
	[6.5, 3.5]])
pred_test_y = model.sim(test_x)
pred_test_labels = []
for pred_test_row in pred_test_y:
	pred_test_row = pred_test_row.astype(int).astype(str)
	pred_test_labels.append('.'.join(pred_test_row))
pred_test_codes = []
for pred_test_label in pred_test_labels:
	pred_test_code = np.where(label_set == pred_test_label)[0][0]
	pred_test_codes.append(pred_test_code)
pred_test_codes = np.array(pred_test_codes)
mp.figure().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Monolayer Neural Network', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x[:, 0], train_x[:, 1], c=train_codes.ravel(),
	cmap='brg', s=80, label='Training')
mp.scatter(test_x[:, 0], test_x[:, 1], c=pred_test_codes.ravel(),
	cmap='brg', s=80, label='Testing', marker='^')
mp.legend()
mp.figure().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Training Progress', fontsize=20)
mp.xlabel('Number Of Epochs', fontsize=14)
mp.ylabel('Training Error', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(error, c='orangered', label='Error')
mp.legend()
mp.show()
