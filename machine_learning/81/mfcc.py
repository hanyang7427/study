import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp
import mpl_toolkits.axes_grid1 as mg
sample_rate, sigs = wf.read(
	'./speeches/training/apple/apple01.wav')
mfcc1 = sf.mfcc(sigs, sample_rate).T
sample_rate, sigs = wf.read(
	'./speeches/training/apple/apple02.wav')
mfcc2 = sf.mfcc(sigs, sample_rate).T
sample_rate, sigs = wf.read(
	'./speeches/training/banana/banana01.wav')
mfcc3 = sf.mfcc(sigs, sample_rate).T
mp.matshow(mfcc1, cmap='gist_rainbow')
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('MFCC-1', fontsize=16)
mp.xlabel('Feature', fontsize=12)
mp.ylabel('Samples', fontsize=12)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(2))
ax.xaxis.set_minor_locator(mp.MultipleLocator())
ax.yaxis.set_major_locator(mp.MultipleLocator(2))
ax.yaxis.set_minor_locator(mp.MultipleLocator())
mp.tick_params(labeltop=False, labelbottom=True, labelsize=10)
mp.matshow(mfcc2, cmap='gist_rainbow')
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('MFCC-2', fontsize=16)
mp.xlabel('Feature', fontsize=12)
mp.ylabel('Samples', fontsize=12)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(2))
ax.xaxis.set_minor_locator(mp.MultipleLocator())
ax.yaxis.set_major_locator(mp.MultipleLocator(2))
ax.yaxis.set_minor_locator(mp.MultipleLocator())
mp.tick_params(labeltop=False, labelbottom=True, labelsize=10)
mp.matshow(mfcc3, cmap='gist_rainbow')
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('MFCC-3', fontsize=16)
mp.xlabel('Feature', fontsize=12)
mp.ylabel('Samples', fontsize=12)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(2))
ax.xaxis.set_minor_locator(mp.MultipleLocator())
ax.yaxis.set_major_locator(mp.MultipleLocator(2))
ax.yaxis.set_minor_locator(mp.MultipleLocator())
mp.tick_params(labeltop=False, labelbottom=True, labelsize=10)
mp.show()
