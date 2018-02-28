import numpy as np
import sklearn.cluster as sc
import sklearn.neighbors as nb
import matplotlib.pyplot as mp
n_samples = 500
t = 2.5 * np.pi * (1 + 2 * np.random.rand(n_samples, 1))
x = 0.05 * t * np.cos(t)
y = 0.05 * t * np.sin(t)
n = 0.05 * np.random.rand(n_samples, 2)
x = np.hstack((x, y)) + n
model1 = sc.AgglomerativeClustering(linkage='average',
	n_clusters=3)
pred_y1 = model1.fit_predict(x)
conn = nb.kneighbors_graph(x, 10, include_self=False)
model2 = sc.AgglomerativeClustering(linkage='average',
	n_clusters=3, connectivity=conn)
pred_y2 = model2.fit_predict(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(121)
mp.title('Non-Connectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x[:, 0], x[:, 1], c=pred_y1, cmap='brg', s=80)
mp.subplot(122)
mp.title('With-Connectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x[:, 0], x[:, 1], c=pred_y2, cmap='brg', s=80)
mp.show()
