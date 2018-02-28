import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
	return dt.datetime.strptime(str(dmy, encoding='utf-8'),'%d-%m-%Y').date().strftime('%Y-%m-%d')

dates, opening_prices, highest_prices, lowest_prices, closing_prices = np.loadtxt(
	'aapl.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), unpack=True, dtype='M8[D],f8,f8,f8,f8',
	converters={1: dmy2ymd})
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Candlestick Chart', fontsize=20)
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
up = closing_prices - opening_prices >= 0.01
down = opening_prices - closing_prices >= 0.01
fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
fc[up], fc[down] = (1, 1, 1), (0, 0.5, 0)
ec[up], ec[down] = (1, 0, 0), (0, 0.5, 0)
mp.bar(dates, highest_prices - lowest_prices, 0,
	lowest_prices, align='center', color=fc, edgecolor=ec)
mp.bar(dates, closing_prices - opening_prices, 0.8,
	opening_prices, align='center', color=fc, edgecolor=ec)
mp.gcf().autofmt_xdate()
mp.show()
'''
print(dates)
print(opening_prices)
print(highest_prices)
print(lowest_prices)
print(closing_prices)
'''
#print(dmy2ymd('28-01-2011'))