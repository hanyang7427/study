import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
	return dt.datetime.strptime(str(dmy, encoding='utf-8'),
		'%d-%m-%Y').date().strftime('%Y-%m-%d')
dates, closing_prices = np.loadtxt(
	'aapl.csv', delimiter=',', usecols=(1, 6),
	unpack=True, dtype='M8[D],f8', converters={1: dmy2ymd})
ma5 = np.zeros(closing_prices.size - (5 - 1))
for i in range(ma5.size):
	ma5[i] = closing_prices[i:i+5].mean()
weights = np.exp(np.linspace(-1, 0, 10))
weights /= weights.sum()
weights = weights[::-1]
ma10 = np.convolve(closing_prices, weights, 'valid')
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Moving Average', fontsize=20)
mp.xlabel('Trading Days', fontsize=14)
mp.ylabel('Stock Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(
	md.DateFormatter('%d %b %Y'))
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, 'o-', c='lightgray',
	label='Closing Price')
mp.plot(dates[5-1:], ma5, c='orangered', label='SMA-5')
mp.plot(dates[10-1:], ma10, c='dodgerblue', label='EMA-10')
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()
