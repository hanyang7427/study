import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(-5, 5, 1001)
y = np.i0(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Bessel Function', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, c='dodgerblue', label='Bessel')
mp.legend()
mp.show()
