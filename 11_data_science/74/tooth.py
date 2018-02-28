import numpy as np
import matplotlib.pyplot as mp
def sawtooth(N):
	k = np.arange(1, N+1)
	def wave(x):
		return (np.sin(2 * k * np.pi * x) / k).sum () * \
			(-2) / np.pi
	return np.frompyfunc(wave, 1, 1)
x = np.linspace(-np.pi, np.pi, 201)
N = 1000
y = sawtooth(N)(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Sawtoothwave', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, 'orangered')
mp.show()
