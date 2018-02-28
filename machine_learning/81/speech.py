import os
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import hmmlearn.hmm as hl
def search_speeches(directory, speeches):
	directory = os.path.normpath(directory)
	for entry in os.listdir(directory):
		label = directory[directory.rfind(os.path.sep) + 1:]
		path = os.path.join(directory, entry)
		if os.path.isdir(path):
			search_speeches(path, speeches)
		elif os.path.isfile(path) and path.endswith('.wav'):
			if label not in speeches:
				speeches[label] = []
			speeches[label].append(path)
speeches = {}
search_speeches('./speeches/training', speeches)
x, y = [], []
for label, filenames in speeches.items():
	mfccs = np.array([])
	for filename in filenames:
		sample_rate, sigs = wf.read(filename)
		mfcc = sf.mfcc(sigs, sample_rate)
		mfccs = mfcc if len(mfccs) == 0 else np.append(mfccs, mfcc, axis=0)
	x.append(mfccs)
	y.append(label)
models = {}
for mfccs, label in zip(x, y):
	model = hl.GaussianHMM(n_components=4, covariance_type='diag',
		n_iter=1000)
	models[label] = model.fit(mfccs)
sample_rate, sigs = wf.read('./speeches/testing/banana/banana15.wav')
mfcc = sf.mfcc(sigs, sample_rate)
best_score, best_label = None, None
for label, model in models.items():
	score = model.score(mfcc)
	if best_score is None:
		best_score = score
	if best_label is None:
		best_label = label
	if best_score < score:
		best_score, best_label = score, label
print(best_label)
