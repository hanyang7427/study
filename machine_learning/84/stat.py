import numpy as np
import pandas as pd
data = np.loadtxt('ts.txt', delimiter=',')
begin_date = '{}-{}'.format(int(data[0, 0]), int (data[0][1]))
end_date = '{}-{}'.format(int(data[-1, 0]) + 1,
	int (data[-1][1]) % 12 + 1)
dates = pd.date_range(begin_date, end_date, freq='M')
ts1 = pd.Series(data[:, 2], index=dates)
ts2 = pd.Series(data[:, 3], index=dates)
df = pd.DataFrame({'ts1': ts1, 'ts2': ts2})
print(df.max())
print(df.max(1))
print(df.min())
print(df.min(1))
print(df.mean())
print(df.mean(1))
print(pd.rolling_mean(df, window=30))
print(df.corr())
print(pd.rolling_corr(df['ts1'], df['ts2'], window=60))


