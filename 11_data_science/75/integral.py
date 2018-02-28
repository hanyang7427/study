import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as mp
import matplotlib.patches as mc
def f(x):
	return 2 * x ** 2 + 3 * x + 4
a, b = -5, 5
x = np.linspace(a, b, 1001)
y = f(x)
mp.figure().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Integral', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, c='red', linewidth=8,
	label=r'$y=2x^2+3x+4$', zorder=0)
n = 100
x = np.linspace(a, b, n + 1)
y = f(x)
for i in range(n):
	mp.gca().add_patch(mc.Polygon([[x[i], 0],
		[x[i], y[i]], [x[i+1], y[i+1]], [x[i+1], 0]],
		fc='dodgerblue', ec='steelblue', alpha=0.5))
area = 0
for i in range(n):
	area += (y[i] + y[i+1]) * (x[i+1] - x[i]) / 2
print(area)
area = si.quad(f, a, b)
print(area)
mp.legend()
mp.show()
