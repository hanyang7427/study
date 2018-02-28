import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
	return dt.datetime.strptime(str(dmy, encoding='utf-8'),
		'%d-%m-%Y').date().strftime('%Y-%m-%d')
dates, closing_prices = np.loadtxt(
	'aapl.csv', delimiter=',', usecols=(1, 6),
	unpack=True, dtype='M8[D],f8', converters={1: dmy2ymd})
N = 3
predicted_prices = np.zeros(
	closing_prices.size - 2 * N + 1)
for i in range(predicted_prices.size):
	a = np.zeros((N, N))
	for j in range(N):
		a[j,] = closing_prices[i+j:i+j+N]
	b = closing_prices[i+N:i+2*N]
	x, _, _, _ = np.linalg.lstsq(a, b)
	predicted_prices[i] = b.dot(x)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Linear Prediction', fontsize=20)
mp.xlabel('Trading Days', fontsize=14)
mp.ylabel('Stock Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(
	md.DateFormatter('%d %b %Y'))
mp.grid(linestyle=':')
closing_dates = dates.astype(md.datetime.datetime)
mp.plot(closing_dates, closing_prices, 'o-', c='lightgray',
	label='Closing Price')
dates = np.append(dates, np.datetime64(
	(pd.to_datetime(str(dates[-1])).date() +
	pd.tseries.offsets.BDay()).strftime('%Y-%m-%d'), 'D'))
predicted_dates = dates[2*N:].astype(md.datetime.datetime)
mp.plot(predicted_dates, predicted_prices, 'o-',
	c='orangered', label='Predicted Price')
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()
