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
bhp_returns = np.diff(
	bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(
	vale_closing_prices) / vale_closing_prices[:-1]
N = 8
weights = np.hanning(N)
weights /= weights.sum()
bhp_han_returns = np.convolve(bhp_returns, weights, 'valid')
vale_han_returns = np.convolve(vale_returns, weights, 'valid')
days = dates[N-1:-1].astype(int)
degree = 5
bhp_p = np.polyfit(days, bhp_han_returns, degree)
vale_p = np.polyfit(days, vale_han_returns, degree)
bhp_poly = np.polyval(bhp_p, days)
vale_poly = np.polyval(vale_p, days)
sub_p = np.polysub(bhp_p, vale_p)
roots = np.roots(sub_p)
reals = roots[np.isreal(roots)].real
min_x, max_x = days.min(), days.max()
inters = []
for real in reals:
	if min_x <= real <= max_x:
		inters.append([real, np.polyval(bhp_p, real)])
inters.sort()
inters = np.array(inters)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Smoothing Returns', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Returns', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates[:-1].astype(md.datetime.datetime)
mp.plot(dates, bhp_returns, c='orangered', alpha=0.25,
	label='BHP')
mp.plot(dates, vale_returns, c='dodgerblue', alpha=0.25,
	label='VALE')
mp.plot(dates[N-1:], bhp_han_returns, c='orangered', alpha=0.75,
	label='BHP')
mp.plot(dates[N-1:], vale_han_returns, c='dodgerblue', alpha=0.75,
	label='VALE')
mp.plot(dates[N-1:], bhp_poly, c='orangered', linewidth=3,
	label='BHP')
mp.plot(dates[N-1:], vale_poly, c='dodgerblue', linewidth=3,
	label='VALE')
dates, inters = np.hsplit(inters, 2)
dates = dates.astype(int).astype('M8[D]').astype(
	md.datetime.datetime)
mp.scatter(dates, inters, marker='x', s=120, c='firebrick', lw=3,
	label='Intersection', zorder=3)
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()




