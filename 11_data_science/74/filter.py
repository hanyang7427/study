import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp
duration = 5
sample_rate = 50
signal_freq = 0.2
times = np.linspace(0, duration, duration * sample_rate)
noised_sigs = np.sin(2 * np.pi * signal_freq * times) + \
	np.random.randn(times.size) / 2
freqs = nf.fftfreq(times.size, d=1 / sample_rate)
noised_ffts = nf.fft(noised_sigs)
noised_amps = np.abs(noised_ffts)
fund_freq = freqs[noised_amps.argmax()]
print(fund_freq)
high_freqs = np.where(np.abs(freqs) > np.abs(fund_freq))
filtered_ffts = noised_ffts.copy()
filtered_ffts[high_freqs] = 0
filtered_amps = noised_amps.copy()
filtered_amps[high_freqs] = 0
filtered_sigs = nf.ifft(filtered_ffts).real
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(221)
mp.title('Noised Signal', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, noised_sigs, c='orangered', label='Noised')
mp.legend()
mp.subplot(222)
mp.title('Noised Amplitude', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Amplitude', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs>=0], noised_amps[freqs>=0],
	c='limegreen', label='Noised')
mp.legend()
mp.subplot(224)
mp.title('Filtered Amplitude', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Amplitude', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs>=0], filtered_amps[freqs>=0],
	c='dodgerblue', label='Filtered')
mp.legend()
mp.subplot(223)
mp.title('Filtered Signal', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, filtered_sigs, c='hotpink', label='Filtered')
mp.legend()
mp.tight_layout()
mp.show()