import numpy as np
import neurolab as nl
import matplotlib.pyplot as mp
x = np.array([
	[0.3, 0.2],
	[0.1, 0.4],
	[0.4, 0.6],
	[0.9, 0.5]])
y = np.array([
	[0],
	[0],
	[0],
	[1]])
model = nl.net.newp([[0, 1], [0, 1]], 1)
error = model.train(x, y, epochs=50, show=1, lr=0.01)
mp.figure().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Neuron', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x[:, 0], x[:, 1], c=y.ravel(), cmap='brg', s=80,
	label='Training')
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
