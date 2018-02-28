import numpy as np
import matplotlib.dates as md
import matplotlib.pyplot as mp
import matplotlib
matplotlib.use('qt4agg')
from matplotlib.font_manager import *

myfont = FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')
matplotlib.rcParams['axes.unicode_minus'] = False

x = [x for x in range(10,19)]
y1 = [4,7,6,12,12,9,8,2,8]
y2 = [8,3,12,38,32,0,19,0,0]
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
# mp.title('', fontsize=20,fontproperties=myfont)
mp.xlabel('日期', fontsize=22,fontproperties=myfont)
mp.ylabel('个数', fontsize=22,fontproperties=myfont)
x = np.array(x)
print(x)
x = x.astype(md.datetime.datetime)
mp.plot(x, y1, 'r-o', label='赞')
mp.plot(x, y2, 'b-o', label='评论数')
mp.legend(prop=myfont)
mp.show()