import numpy as np
import neurolab as nl
import matplotlib.pyplot as mp
train_x = np.linspace(-10, 10, 100)
train_y = 2 * np.square(train_x) + 7
train_y /= np.linalg.norm(train_y)
train_x = train_x.reshape(-1, 1)
train_y = train_y.reshape(-1, 1)
model = nl.net.newff([[train_x.min(), train_x.max()]], [10, 10, 1])
model.trainf = nl.train.train_gd
error = model.train(train_x, train_y, epochs=800, show=100,
	goal=0.01)
test_x = np.linspace(-10, 10, 1000)
test_x = test_x.reshape(-1, 1)
pred_test_y = model.sim(test_x)
mp.figure().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Deep Neural Network', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_x, train_y, c='dodgerblue', label='Training')
mp.plot(test_x, pred_test_y, c='limegreen', label='Testing')
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
