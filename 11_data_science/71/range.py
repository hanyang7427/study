import numpy as np
highest_prices, lowest_prices = np.loadtxt('aapl.csv',
	delimiter=',', usecols=(3, 4), unpack=True)
max_highest_price = np.max(highest_prices)
min_lowest_price = np.min(lowest_prices)
range_price = max_highest_price - min_lowest_price
print(range_price)
max_highest_price = highest_prices[0]
min_lowest_price = lowest_prices[0]
for highest_price, lowest_price in zip(highest_prices,
	lowest_prices):
	if highest_price > max_highest_price:
		max_highest_price = highest_price
	if lowest_price < min_lowest_price:
		min_lowest_price = lowest_price
range_price = max_highest_price - min_lowest_price
print(range_price)
