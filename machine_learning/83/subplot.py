import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
data = np.loadtxt('ts.txt', delimiter=',')
begin_date = '{}-{}'.format(int(data[0, 0]), int (data[0][1]))
end_date = '{}-{}'.format(int(data[-1, 0]) + 1,
	int (data[-1][1]) % 12 + 1)
dates = pd.date_range(begin_date, end_date, freq='M')
ts1 = pd.Series(data[:, 2], index=dates)
ts2 = pd.Series(data[:, 3], index=dates)
df = pd.DataFrame({'ts1': ts1, 'ts2': ts2})
df = df['2014-1':'2015-1']
title = 'From {} to {}'.format(ts1.index[0].strftime('%b %Y'),
	ts1.index[-1].strftime('%b %Y'))
axes = df.plot(subplots=True, marker='o',
	color=['dodgerblue', 'orangered'], title=[title, title])
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
for ax in axes:
	ax.set_xlabel('Time', fontsize=14)
	ax.set_ylabel('Data', fontsize=14)
	ax.tick_params(labelsize=10)
	ax.grid(linestyle=':')
mp.show()