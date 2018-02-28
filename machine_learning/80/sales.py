import csv
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
with open('sales.csv', 'r') as f:
	reader = csv.reader(f)
	x = []
	for row in reader:
		x.append(row)
feature_names = np.array(x[0])[[3, 4]]
x = np.array(x)[1:, [3, 4]].astype(float)
bw = sc.estimate_bandwidth(x, n_samples=len(x), quantile=0.8)
model = sc.MeanShift(bandwidth=bw, bin_seeding=True)
model.fit(x)
centers = model.cluster_centers_
pred_y = model.predict(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Sales Cluster', fontsize=20)
mp.xlabel(feature_names[0], fontsize=14)
mp.ylabel(feature_names[1], fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=80)
mp.scatter(centers[:, 0], centers[:, 1], marker='+',
	c='black', s=1000, linewidth=1)
mp.show()
