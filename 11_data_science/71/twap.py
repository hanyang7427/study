import datetime as dt
import numpy as np
def dmy2days(dmy):
	return (dt.datetime.strptime(str(dmy, encoding='utf-8'),
		'%d-%m-%Y').date() - dt.date.min).days
times, closing_prices = np.loadtxt('aapl.csv', delimiter=',',
	usecols=(1, 6), unpack=True, converters={1: dmy2days})
twap = np.average(closing_prices, weights=times)
print(twap)
twap, tsum = 0, 0
for closing_price, time in zip(closing_prices, times):
	twap += closing_price * time
	tsum += time
twap /= tsum
print(twap)
