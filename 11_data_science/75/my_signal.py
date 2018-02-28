import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
mp.figure().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
ax = mp.gca()
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
line = mp.plot([], [], c='orangered', label='Signal')[0]
mp.legend()
line.set_data([], [])
def update(data):
	t, s = data
	x, y = line.get_data()
	x.append(t)
	y.append(s)
	ax = mp.gca()
	x_min, x_max = ax.get_xlim()
	if t >= x_max:
		ax.set_xlim(x_min, x_max * 2)
		ax.figure.canvas.draw()
	line.set_data(x, y)
def generator():
	t = 0
	for i in range(10000):
		s = np.sin(2 * np.pi * t) * np.exp(-t / 8)
		yield t, s
		t += 0.05
anim = ma.FuncAnimation(mp.gcf(), update, generator,
	blit=False, interval=5, repeat=False)
mp.show()
