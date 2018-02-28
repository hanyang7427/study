import os
import warnings
import numpy as np
import cv2 as cv
import hmmlearn.hmm as hl
warnings.filterwarnings('ignore', category=DeprecationWarning)
np.seterr(all='ignore')
train_dir = 'objects\\training'
if not os.path.isdir(train_dir):
	raise IOError(
		"The directory '" + train_dir + "' doesn't exist!")
train_objs = {}
for curdir, subdirs, files in os.walk(train_dir):
	for jpeg in (file for file in files if file.endswith('.jpg')):
		path = os.path.join(curdir, jpeg)
		label = path.split(os.path.sep)[-2]
		if label not in train_objs:
			train_objs[label] = []
		train_objs[label].append(path)
x, y = [], []
for label, filenames in train_objs.items():
	descs = np.array([])
	for filename in filenames:
		image = cv.imread(filename)
		h, w = image.shape[:2]
		scale = 200 / min(h, w)
		image = cv.resize(image, None, fx=scale, fy=scale)
		star = cv.xfeatures2d.StarDetector_create()
		keypoints = star.detect(image)
		sift = cv.xfeatures2d.SIFT_create()
		_, desc = sift.compute(image, keypoints)
		if len(descs) == 0:
			descs = desc
		else:
			descs = np.append(descs, desc, axis=0)
	x.append(descs)
	y.append(label)
models = {}
for descs, label in zip(x, y):
	model = hl.GaussianHMM(n_components=4,
		covariance_type='diag', n_iter=1000)
	models[label] = model.fit(descs)
filename = 'objects\\testing\\motorbike\\0020.jpg'
image = cv.imread(filename)
h, w = image.shape[:2]
scale = 200 / min(h, w)
image = cv.resize(image, None, fx=scale, fy=scale)
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(image)
sift = cv.xfeatures2d.SIFT_create()
_, desc = sift.compute(image, keypoints)
best_score, best_label = None, None
for label, model in models.items():
	score = model.score(desc)
	if (best_score == None) or (best_score < score):
		best_score = score
		best_label = label
print(best_label)
