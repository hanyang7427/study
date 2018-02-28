import numpy as np
import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
np.random.seed(7)
x, y = sd.make_circles(n_samples=500, factor=0.2,
	noise=0.04)
model = dc.PCA()
pca_x = model.fit_transform(x)
model = dc.KernelPCA(kernel='rbf',
	fit_inverse_transform=True, gamma=10)
kpca_x = model.fit_transform(x)
ikpca_x = model.inverse_transform(kpca_x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(221)
mp.title('Original Samples', fontsize=16)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x[y == 0][:, 0], x[y == 0][:, 1],
	s = 80, c='dodgerblue', alpha=0.5, label='Class 0')
mp.scatter(x[y == 1][:, 0], x[y == 1][:, 1],
	s = 80, c='orangered', alpha=0.5, label='Class 1')
mp.legend()
mp.subplot(222)
mp.title('PCA Samples', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(pca_x[y == 0][:, 0], pca_x[y == 0][:, 1],
	s = 80, c='dodgerblue', alpha=0.5, label='Class 0')
mp.scatter(pca_x[y == 1][:, 0], pca_x[y == 1][:, 1],
	s = 80, c='orangered', alpha=0.5, label='Class 1')
mp.legend()
mp.subplot(223)
mp.title('KPCA Samples', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(kpca_x[y == 0][:, 0], kpca_x[y == 0][:, 1],
	s = 80, c='dodgerblue', alpha=0.5, label='Class 0')
mp.scatter(kpca_x[y == 1][:, 0], kpca_x[y == 1][:, 1],
	s = 80, c='orangered', alpha=0.5, label='Class 1')
mp.legend()
mp.subplot(224)
mp.title('Inverse KPCA Samples', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(ikpca_x[y == 0][:, 0], ikpca_x[y == 0][:, 1],
	s = 80, c='dodgerblue', alpha=0.5, label='Class 0')
mp.scatter(ikpca_x[y == 1][:, 0], ikpca_x[y == 1][:, 1],
	s = 80, c='orangered', alpha=0.5, label='Class 1')
mp.legend()
mp.tight_layout()
mp.show()
