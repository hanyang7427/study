import numpy as np
closing_prices = np.loadtxt('aapl.csv',
	delimiter=',', usecols=(6), unpack=True)
diff_prices = np.diff(closing_prices)
rets = diff_prices / closing_prices[:-1]
ret_std = np.std(rets)
print(ret_std)