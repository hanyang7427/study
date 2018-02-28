import os
import numpy as np
import cv2 as cv
import sklearn.preprocessing as sp
face_detector = cv.CascadeClassifier('haar\\face.xml')


def read_data(directory):
	if not os.path.isdir(directory):
		raise IOError("The directory '", derector,
			"' doesn't exist!")
	faces_dir = {}
	for curdir, subdirs, files in os.walk(directory):
		for jpeg in (
			file for file in files if file.endswith('.jpg')):
			path = os.path.join(curdir, jpeg)
			label = path.split(os.path.sep)[-2]
			if label not in faces_dir:
				faces_dir[label] = []
			else:
				faces_dir[label].append(path)
	codec = sp.LabelEncoder()
	codec.fit(list(faces_dir.keys()))
	x, y, z = [], [], []
	for label, filenames in faces_dir.items():
		for filename in filenames:
			bgr = cv.imread(filename)
			gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
			faces = face_detector.detectMultiScale(
				gray, 1.1, 2, minSize=(100, 100))
			for l, t, w, h in faces:
				x.append(gray[t:t + h, l:l + w])
				y.append(int(codec.transform([label])[0]))
				a, b = int(w / 2), int(h / 2)
				cv.ellipse(bgr, (l + a, t + b), (a, b),
					0, 0, 360, (255, 0, 255), 2)
				z.append(bgr)
	y = np.array(y)
	return codec, x, y, z
codec, train_x, train_y, train_z = read_data(
	'faces\\training')
_, test_x, test_y, test_z = read_data(
	'faces\\testing')
# 局部二值模式直方人脸识别模型
model = cv.face.LBPHFaceRecognizer_create()
model.train(train_x, train_y)
pred_test_y = []
for x in test_x:
	y = model.predict(x)
	pred_test_y.append(y[0])
escape = False
while not escape:
	for code, pred_code, image in zip(
		test_y, pred_test_y, test_z):
		label = codec.inverse_transform([code])[0]
		pred_label = codec.inverse_transform(
			[pred_code])[0]
		text = '{} {} {}'.format(label,
			'==' if label == pred_label else '!=', pred_label)
		cv.putText(image, text, (10, 60),
			cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 6)
		cv.imshow('Recognizing Face...', image)
		if cv.waitKey(1000) == 27:
			escape = True
			break;





