import numpy as np
dates, highest_prices, lowest_prices, \
	closing_prices = np.loadtxt(
	'aapl.csv', delimiter=',', usecols=(1, 4, 5, 6),
	unpack=True, dtype='U10,f8,f8,f8')
N = 20
dates = dates[-N-1:]
highest_prices = highest_prices[-N:]
lowest_prices = lowest_prices[-N:]
closing_prices = closing_prices[-N-1:-1]
hc = highest_prices - closing_prices
cl = closing_prices - lowest_prices
hl = highest_prices - lowest_prices
tr = np.maximum(np.maximum(hc, cl), hl)
atr = np.zeros(N)
for i in range(N):
	if i == 0:
		atr[i] = tr.mean()
	else:
		atr[i] = (atr[i-1] * (N - 1) + tr[i]) / N
print(atr)