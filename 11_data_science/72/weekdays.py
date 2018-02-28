import datetime as dt
import numpy as np
#             0     1     2     3     4     5     6
g_weekdays=('MON','TUE','WED','THU','FRI','SAT','SUN')
def dmy2weekday(dmy):
	return dt.datetime.strptime(str(dmy, encoding='utf-8'),
		'%d-%m-%Y').date().weekday()
weekdays, closing_prices = np.loadtxt(
	'aapl.csv', delimiter=',', usecols=(1, 6),
	unpack=True, converters={1: dmy2weekday})
average_prices = np.zeros(5)
for weekday in range(average_prices.size):
	'''
	average_prices[weekday] = np.take(closing_prices,
		np.where(weekdays == weekday)).mean()
	'''
	average_prices[weekday] = closing_prices[
		weekdays == weekday].mean()
for i, average_price in enumerate(average_prices):
	print(g_weekdays[i], np.round(average_price, 2))
