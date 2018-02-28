import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp
times = np.linspace(0, 2 * np.pi, 201)
sigs1 = 4 * np.sin(1 * times) / (1 * np.pi)
sigs2 = 4 * np.sin(3 * times) / (3 * np.pi)
sigs3 = 4 * np.sin(5 * times) / (5 * np.pi)
sigs4 = 4 * np.sin(7 * times) / (7 * np.pi)
sigs5 = 4 * np.sin(9 * times) / (9 * np.pi)
sigs0 = sigs1 + sigs2 + sigs3 + sigs4 + sigs5
freqs = nf.fftfreq(times.size, d=times[1] - times[0])
ffts = nf.fft(sigs0)
amps = np.abs(ffts)
sigsi = nf.ifft(ffts)
sigsr = sigsi.real
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(121)
mp.title('Time Domain', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, sigs1,
	label='{:.4f}'.format(1 / (2 * np.pi)))
mp.plot(times, sigs2,
	label='{:.4f}'.format(3 / (2 * np.pi)))
mp.plot(times, sigs3,
	label='{:.4f}'.format(5 / (2 * np.pi)))
mp.plot(times, sigs4,
	label='{:.4f}'.format(7 / (2 * np.pi)))
mp.plot(times, sigs5,
	label='{:.4f}'.format(9 / (2 * np.pi)))
mp.plot(times, sigs0,
	label='{:.4f}'.format(1 / (2 * np.pi)))
mp.plot(times, sigsr, c='gray', alpha=0.5, linewidth=5,
	label='{:.4f}'.format(1 / (2 * np.pi)))
mp.legend()
mp.subplot(122)
mp.title('Frequency Domain', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Amplitude', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs>=0], amps[freqs>=0], c='orangered')
mp.show()
