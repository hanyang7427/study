import numpy as np
import matplotlib.pyplot as mp
A, a, B, b = 10, 9, 5, 8
#A, a, B, b = 10, 1, 5, 1
#A, a, B, b = 10, 1, 5, 2
#A, a, B, b = 10, 1, 5, 3
t = np.linspace(-np.pi, np.pi, 201)
x = A * np.sin(a * t + np.pi / 2)
y = B * np.sin(b * t)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Lissajous', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, 'orangered')
mp.show()
