import warnings
import numpy as np
import hmmlearn.hmm as hl
import matplotlib.pyplot as mp
warnings.filterwarnings('ignore', category=DeprecationWarning)
data = np.loadtxt('hmm.txt', delimiter=',')
train_y = np.column_stack([data[:, 2]])
train_x = np.arange(len(train_y))
model = hl.GaussianHMM(n_components=4, covariance_type='diag',
	n_iter=1000)
model.fit(train_y)
print(model.means_)
print(model.covars_)
train_z = model.predict(train_y)
test_x = np.arange(int(len(train_x / 2)))
test_y, test_z = model.sample(len(test_x))
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(211)
mp.title('Train Sample', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Sample', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, c=train_z,
	cmap='tab10', alpha=0.25, s=80)
mp.plot(train_x, train_y, c='black', linewidth=1, label='Train')
mp.legend()
mp.subplot(212)
mp.title('Test Sample', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Sample', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(test_x, test_y, c=test_z,
	cmap='tab10', alpha=0.25, s=80)
mp.plot(test_x, test_y, c='black', linewidth=1, label='Test')
mp.legend()
mp.tight_layout()
mp.show()
