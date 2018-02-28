import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	ymd = date.strftime('%Y-%m-%d')
	return ymd
dates, bhp_closing_prices = np.loadtxt('bhp.csv',
	delimiter=',', usecols=(1, 6), unpack=True,
	dtype='M8[D],f8', converters={1: dmy2ymd})
_, vale_closing_prices = np.loadtxt('vale.csv',
	delimiter=',', usecols=(1, 6), unpack=True,
	dtype='M8[D],f8', converters={1: dmy2ymd})
diff_closing_prices = \
	bhp_closing_prices - vale_closing_prices
days = dates.astype(int)
degree = 5
p = np.polyfit(days, diff_closing_prices, degree)
polys = np.polyval(p, days)
d = np.polyder(p)
roots = np.roots(d)
reals = roots[np.isreal(roots)].real
min_x, max_x = days.min(), days.max()
peeks = [[min_x, np.polyval(p, min_x)]]
for real in reals:
	if min_x < real and real < max_x:
		peeks.append([real, np.polyval(p, real)])
peeks.append([max_x, np.polyval(p, max_x)])
peeks.sort()
peeks = np.array(peeks)
print(peeks)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Polynomial Fitting', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Difference Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, diff_closing_prices, 's', c='limegreen',
	label='Difference Price')
mp.plot(dates, polys, c='orangered',
	label='Polynomail Fitting')
dates, peeks = np.hsplit(peeks, 2)
dates = dates.astype(int).astype('M8[D]').astype(
	md.datetime.datetime)
mp.plot(dates, peeks, '^', c='dodgerblue', label='Peek')
for i in range(1, dates.size):
	mp.annotate('', xytext=(dates[i-1], peeks[i-1]),
		xy=(dates[i], peeks[i]), size=30, arrowprops=dict(
		arrowstyle='fancy', connectionstyle='arc3',
		fc='pink', ec='none', lw=0))
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()




