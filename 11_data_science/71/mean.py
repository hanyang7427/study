import numpy as np
closing_prices = np.loadtxt('aapl.csv', delimiter=',',
	usecols=(6), unpack=True)
mean = np.mean(closing_prices)
print(mean)
mean = 0
for closing_price in closing_prices:
	mean += closing_price
mean /= closing_prices.size
print(mean)