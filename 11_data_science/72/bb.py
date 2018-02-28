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
N = 5
weights = np.ones(N) / N
medios = np.convolve(closing_prices, weights, 'valid')
stds = []
for i in range(medios.size):
	stds.append(np.std(closing_prices[i:i+N]))
stds = np.array(stds)
double_stds = stds * 2
lowers = medios - double_stds
uppers = medios + double_stds
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Bollinger Bands', fontsize=20)
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
mp.plot(dates[N-1:], medios, c='dodgerblue', label='Medio')
mp.plot(dates[N-1:], lowers, c='limegreen', label='Lower')
mp.plot(dates[N-1:], uppers, c='orangered', label='Upper')
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()
