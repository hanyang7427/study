import datetime as dt
import numpy as np
def dmy2weekday(dmy):
	return dt.datetime.strptime(str(dmy, encoding='utf-8'),
		'%d-%m-%Y').date().weekday()
weekdays, opening_prices, highest_prices, lowest_prices, \
	closing_prices = np.loadtxt(
	'aapl.csv', delimiter=',', usecols=(1, 3, 4, 5, 6),
	unpack=True, converters={1: dmy2weekday})
weekdays = weekdays[:16]
opening_prices = opening_prices[:16]
highest_prices = highest_prices[:16]
lowest_prices = lowest_prices[:16]
closing_prices = closing_prices[:16]
def summary(week_indices):
	opening_price = opening_prices[week_indices[0]]
	highest_price = np.take(highest_prices,
		week_indices).max()
	lowest_price = np.take(lowest_prices,
		week_indices).min()
	closing_price = closing_prices[week_indices[-1]]
	return opening_price, highest_price, lowest_price, \
		closing_price
first = np.where(weekdays == 0)[0][0]
last = np.where(weekdays == 4)[0][-1]
indices = np.arange(first, last+1)
indices = np.split(indices, 3)
summaries = np.apply_along_axis(summary, 1, indices)
print(summaries)

