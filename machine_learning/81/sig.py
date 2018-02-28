import numpy as np
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp
sample_rate, sigs = wf.read('signal.wav')
sigs = sigs[:30] / 2 ** 15
times = np.arange(30) / sample_rate
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Audio Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, sigs, c='dodgerblue', label='Signal', zorder=0)
mp.scatter(times, sigs, edgecolor='orangered',
	facecolor='white', s=80, label='Sample', zorder=1)
mp.legend()
mp.show()
