import numpy as np
highest_prices, lowest_prices = np.loadtxt('aapl.csv',
	delimiter=',', usecols=(3, 4), unpack=True)
highest_spread = np.ptp(highest_prices)
lowest_spread = np.ptp(lowest_prices)
print(highest_spread, lowest_spread)
max_highest_price = highest_prices[0]
min_highest_price = highest_prices[0]
max_lowest_price = lowest_prices[0]
min_lowest_price = lowest_prices[0]
for highest_price, lowest_price in zip(highest_prices,
	lowest_prices):
	if highest_price > max_highest_price:
		max_highest_price = highest_price
	if highest_price < min_highest_price:
		min_highest_price = highest_price
	if lowest_price > min_lowest_price:
		max_lowest_price = lowest_price
	if lowest_price < min_lowest_price:
		min_lowest_price = lowest_price
high_spread = max_highest_price - min_highest_price
low_spread = max_lowest_price - min_lowest_price
print(highest_spread, lowest_spread)
