import numpy as np
closing_prices = np.loadtxt('aapl.csv',
	delimiter=',', usecols=(6), unpack=True)
closing_prices = closing_prices[:-1]
median_price = np.median(closing_prices)
print(median_price)
sorted_closing_prices = np.msort(closing_prices)
n=sorted_closing_prices.size
print(n)
median_price = (sorted_closing_prices[int((n-1)/2)] +
	sorted_closing_prices[int(n/2)]) / 2
print(median_price)