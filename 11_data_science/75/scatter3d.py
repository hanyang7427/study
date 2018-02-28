import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
closing_prices, volumes = np.loadtxt(
	'goog.csv', delimiter=',', usecols=(4, 6),
	unpack=True, skiprows=1)
closing_price_rates = np.diff(
	closing_prices) / closing_prices[:-1]
volume_rates = np.diff(volumes) / volumes[:-1]
ax = mp.gca(projection='3d')
mp.title('Scatter Chart', fontsize=20)
ax.set_xlabel('Price', fontsize=14)
ax.set_ylabel('volume', fontsize=14)
ax.set_zlabel('Rate', fontsize=14)
mp.tick_params(labelsize=10)
# X坐标表示收盘价，Y坐标表示成交量，
# Z坐标表示收盘价增长率，颜色表示成交量增长率
ax.scatter(closing_prices[:-1], volumes[:-1],
	closing_price_rates, c=volume_rates, cmap='prism',
	label='Price-Volume')
mp.legend()
mp.show()
