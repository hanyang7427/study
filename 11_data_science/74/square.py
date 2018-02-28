import numpy as np
import matplotlib.pyplot as mp
def square(N):
	k = np.arange(1, 2 * N, 2)
	def wave(x):
		return (np.sin(k * x) / k).sum () * 4 / np.pi
	return np.frompyfunc(wave, 1, 1)
x = np.linspace(-np.pi, np.pi, 201)
N = 1000
y = square(N)(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Squarewave', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, 'orangered')
mp.show()
