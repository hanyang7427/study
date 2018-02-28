import numpy as np
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
x = np.loadtxt('signals.txt')
model = dc.FastICA(n_components=x.shape[1])
ica_x = model.fit_transform(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(221)
mp.title('Original', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x.sum(axis=1), c='dodgerblue', label='Mixture')
mp.legend()
mp.subplot(222)
mp.title('Original Componets', fontsize=16)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
for i, componet in enumerate(x.T):
	mp.plot(componet, label='Component %d' % (i + 1))
mp.legend()
mp.subplot(223)
mp.title('ICA Componets', fontsize=16)
mp.xlabel('Timel', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
for i, componet in enumerate(ica_x.T):
	mp.plot(componet, label='Component %d' % (i + 1))
mp.legend()
mp.subplot(224)
mp.title('ICA Samples', fontsize=16)
mp.xlabel('Timel', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(ica_x.sum(axis=1), c='orangered', label='Mixture')
mp.legend()
mp.tight_layout()
mp.show()