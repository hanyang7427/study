import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	ymd = date.strftime('%Y-%m-%d')
	return ymd
dates, opening_prices, highest_prices, lowest_prices, \
	closing_prices = np.loadtxt('bhp.csv',
	delimiter=',', usecols=(1, 3, 4, 5, 6), unpack=True,
	dtype='M8[D],f8,f8,f8,f8', converters={1: dmy2ymd})
def calc_profit(buying_rate, opening_price, highest_price,
	lowest_price, closing_price):
	buying_price = opening_price * buying_rate
	if lowest_price <= buying_price <= highest_price:
		profit = (closing_price - \
			buying_price) * 100 / buying_price
	else:
		profit = None
	return profit
buring_rates = np.zeros_like(closing_prices)
buring_rates.fill(0.9985)
profits = np.vectorize(calc_profit)(buring_rates,
	opening_prices, highest_prices, lowest_prices,
	closing_prices)
nan = np.isnan(profits)
dates, profits = dates[~nan], profits[~nan]
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Trading Simulation', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Profit', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, profits, c='gray', label='Profit')
ave_profits = np.empty_like(profits)
ave_profits.fill(profits.mean())
mp.plot(dates, ave_profits, '--', c='gray', linewidth=1,
	label='Average Profit')
gain_dates, gains = dates[profits > 0], \
	profits[profits > 0]
mp.plot(gain_dates, gains, 'o', c='orangered',
	label='Gain')
ave_gains = np.empty_like(gains)
ave_gains.fill(gains.mean() if gains.size > 0 else 0)
mp.plot(gain_dates, ave_gains, '--', c='orangered',
	linewidth=1, label='Average Gain')
loss_dates, losses = dates[profits < 0], \
	profits[profits < 0]
mp.plot(loss_dates, losses, 'o', c='dodgerblue',
	label='Loss')
ave_losses = np.empty_like(losses)
ave_losses.fill(losses.mean() if losses.size > 0 else 0)
mp.plot(loss_dates, ave_losses, '--', c='dodgerblue',
	linewidth=1, label='Average Loss')
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()




