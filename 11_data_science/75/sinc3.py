import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
u = np.linspace(-2.5, 2.5, 501)
x, y = np.meshgrid(u, u)
z = np.sinc(x * y)
ax = mp.gca(projection='3d')
mp.title('3D Surface', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
ax.plot_surface(x, y, z, rstride=5, cstride=5,
	cmap='jet')
mp.show()
