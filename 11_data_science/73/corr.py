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
ave_a = np.mean(bhp_returns)
dev_a = bhp_returns - ave_a
var_a = np.mean(dev_a * dev_a)
#std_a = np.sqrt(var_a)
std_a = np.std (bhp_returns, ddof=1)
ave_b = np.mean(vale_returns)
dev_b = vale_returns - ave_b
var_b = np.mean(dev_b * dev_b)
#std_b = np.sqrt(var_b)
std_b = np.std(vale_returns, ddof=1)
cov_aa = var_a
cov_ab = np.mean(dev_a * dev_b)
cov_ba = np.mean(dev_b * dev_a)
cov_bb = var_b
'''
covs = np.array([
	[cov_aa, cov_ab],
	[cov_ba, cov_bb]])
'''
covs = np.cov(bhp_returns, vale_returns)
stds = np.array([
	[std_a * std_a, std_a * std_b],
	[std_b * std_a, std_b * std_b]])
corr = covs / stds
print(corr)
corr = np.corrcoef(bhp_returns, vale_returns)
print(corr)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Correlation Of Returns', fontsize=20)
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
mp.plot(dates, bhp_returns, 'o-', c='orangered',
	label='BHP')
mp.plot(dates, vale_returns, 'o-', c='limegreen',
	label='VALE')
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()




