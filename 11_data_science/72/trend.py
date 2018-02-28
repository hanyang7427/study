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
days = dates.astype(int)
a = np.column_stack((days, np.ones(days.size)))
x = np.linalg.lstsq(a, closing_prices)[0]
k, b = x[0], x[1]
predicted_prices = k * days + b
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Linear Regression', fontsize=20)
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
mp.plot(dates, predicted_prices, c='orangered',
	label='Predicted Price')
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()
