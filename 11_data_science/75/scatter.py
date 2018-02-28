import numpy as np
import matplotlib.pyplot as mp
closing_prices, volumes = np.loadtxt(
	'goog.csv', delimiter=',', usecols=(4, 6),
	unpack=True, skiprows=1)
closing_price_rates = np.diff(
	closing_prices) / closing_prices[:-1]
volume_rates = np.diff(volumes) / volumes[:-1]
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Scatter Chart', fontsize=20)
mp.xlabel('Price', fontsize=14)
mp.ylabel('volume', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 水平坐标表示收盘价，垂直坐标表示成交量，
# 点的大小表示收盘价增长率，颜色表示成交量增长率
mp.scatter(closing_prices[:-1], volumes[:-1],
	s=closing_price_rates * 10000,
	c=volume_rates, cmap='prism', label='Price-Volume')
mp.legend()
mp.show()
