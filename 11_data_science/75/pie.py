import numpy as np
import matplotlib.pyplot as mp
values = [40000, 30000, 15000, 10000, 5000]
spaces = [0.1, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'C++', 'PHP', 'Java', 'Ruby']
colors = ['dodgerblue', 'orangered', 'limegreen',
	'violet', 'gold']
mp.figure().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Programming Language', fontsize=20)
mp.pie(values, spaces, labels, colors, '%d%%',
	shadow=True, startangle=90)
mp.axis('equal')
mp.show()