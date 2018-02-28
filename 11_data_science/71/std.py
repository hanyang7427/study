import numpy as np
closing_prices = np.loadtxt('aapl.csv',
	delimiter=',', usecols=(6), unpack=True)
var = np.var(closing_prices)
std = np.std(closing_prices)
print(var, std)
mean = closing_prices.mean()
devs = closing_prices - mean
dev2 = devs ** 2
var = dev2.mean()
std = np.sqrt(var)
print(var, std)