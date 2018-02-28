import numpy as np
import matplotlib.pyplot as mp
samples = np.random.normal (size=10000)
print(samples)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Normal Distribution', fontsize=20)
mp.xlabel('Sample', fontsize=14)
mp.ylabel('Occurrence', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制正态分布随机样本直方图
_, bins, _ = mp.hist(samples, int(np.sqrt(samples.size)),
	normed=True, edgecolor='steelblue',
	facecolor='deepskyblue')
prob_dens = np.exp(-bins ** 2 / 2) / np.sqrt(2 * np.pi)
mp.plot(bins, prob_dens, 'o-', c='orangered',
	label='Probability Density')
mp.legend()
mp.show()
