import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	ymd = date.strftime('%Y-%m-%d')
	return ymd
dates, closing_prices, volumes = np.loadtxt('bhp.csv',
	delimiter=',', usecols=(1, 6, 7), unpack=True,
	dtype='M8[D],f8,f8', converters={1: dmy2ymd})
diffs = np.diff(closing_prices)
#signs = np.sign(diffs)
signs = np.piecewise(diffs,
	[diffs < 0, diffs == 0, diffs > 0], [-1, 0, 1])
obvs = volumes[1:] * signs
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('On-Balance Volume', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('OBV', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates[1:].astype(md.datetime.datetime)
up = obvs > 0
down = obvs < 0
fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
fc[up], fc[down] = (1, 0, 0), (0, 0.5, 0)
ec[up], ec[down] = (1, 1, 1), (1, 1, 1)
mp.bar(dates, obvs, 1.0, 0, align='center', color=fc,
	edgecolor=ec, label='OBV')
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()




