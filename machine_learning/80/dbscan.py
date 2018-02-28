import numpy as np
import sklearn.cluster as sc
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x = []
with open('perf.txt', 'r') as f:
	for line in f.readlines():
		data = [float(substr) for substr in line.split(',')]
		x.append(data)
x = np.array(x)
epsilons, scores, models = np.linspace(0.3, 1.2, 10), [], []
for epsilon in epsilons:
	model = sc.DBSCAN(eps=epsilon, min_samples=5)
	model.fit(x)
	score = sm.silhouette_score(x, model.labels_,
		sample_size=len(x), metric='euclidean')
	scores.append(score)
	models.append(model)
scores = np.array(scores)
print(epsilons)
print(scores)
best_index = scores.argmax()
print(epsilons[best_index])
print(scores[best_index])
best_model = models[best_index]
pred_y = best_model.fit_predict(x)
core_mask = np.zeros(len(x), dtype=bool)
core_mask[best_model.core_sample_indices_] = True
offset_mask = best_model.labels_ == -1
periphery_mask = ~(core_mask | offset_mask)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('DBSCAN Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
labels = set(pred_y)
cs = mp.get_cmap('brg', len(labels))(range(len(labels)))
mp.scatter(x[core_mask][:, 0], x[core_mask][:, 1],
	c=cs[pred_y[core_mask]], cmap='brg', s=80)
mp.scatter(x[offset_mask][:, 0], x[offset_mask][:, 1],
	c=cs[pred_y[offset_mask]], cmap='brg', s=80, marker='x')
mp.scatter(x[periphery_mask][:, 0], x[periphery_mask][:, 1],
	edgecolor=cs[pred_y[periphery_mask]], facecolor='none',
	cmap='brg', s=80)
mp.show()
