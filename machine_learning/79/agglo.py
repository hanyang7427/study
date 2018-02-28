import numpy as np
import sklearn.cluster as sc
import sklearn.neighbors as nb
import matplotlib.pyplot as mp
x = []
with open('multiple.txt', 'r') as f:
	for line in f.readlines():
		data = [float(substr) for substr in line.split(',')]
		x.append(data)
x = np.array(x)
model = sc.AgglomerativeClustering(linkage='ward',
	n_clusters=4)
'''
conn = nb.kneighbors_graph(x, 10, include_self=False)
model = sc.AgglomerativeClustering(linkage='average',
	n_clusters=8, connectivity=conn)
'''
pred_y = model.fit_predict(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Agglomerative Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=80)
mp.show()





