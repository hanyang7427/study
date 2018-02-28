import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp
sample_rate, sigs = wf.read('noised.wav')
sigs = sigs / 2 ** 15
times = np.arange(len(sigs)) / sample_rate
freqs = nf.fftfreq(sigs.size, d=1 / sample_rate)
ffts = nf.fft(sigs)
amps = np.abs(ffts)
fund_freq = np.abs(freqs[amps.argmax()])
high_freq = np.where(np.abs(freqs) != fund_freq)
filter_ffts = ffts.copy()
filter_ffts[high_freq] = 0
filter_amps = np.abs(filter_ffts)
filter_sigs = nf.ifft(filter_ffts).real
wf.write('filter.wav', sample_rate,
	(filter_sigs * 2 ** 15).astype(np.int16))
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(221)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:200], sigs[:200], c='dodgerblue', label='Signal')
mp.legend()
mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(freqs[freqs>=0], amps[freqs>=0], c='orangered',
	label='Power')
mp.legend()
mp.subplot(224)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs>=0], filter_amps[freqs>=0],
	c='limegreen', label='Power')
mp.legend()
mp.subplot(223)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:200], filter_sigs[:200], c='hotpink',
	label='Signal')
mp.legend()
mp.tight_layout()
mp.show()
