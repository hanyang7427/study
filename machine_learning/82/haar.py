import numpy as np
import cv2 as cv
face_detector = cv.CascadeClassifier('haar\\face.xml')
eye_detector = cv.CascadeClassifier('haar\\eye.xml')
nose_detector = cv.CascadeClassifier('haar\\nose.xml')
cap = cv.VideoCapture(0)
while True:
	image = cap.read()[1]
	faces = face_detector.detectMultiScale(image, 1.3, 5)
	eyes = eye_detector.detectMultiScale(image, 1.3, 5)
	noses = nose_detector.detectMultiScale(image, 1.3, 5)
	for l, t, w, h in faces:
		a, b = int(w / 2), int(h / 2)
		cv.ellipse(image, (l + a, t + b), (a, b), 0, 0, 360,
			(0, 0, 255), 2)
	for l, t, w, h in eyes:
		a, b = int(w / 2), int(h / 2)
		cv.ellipse(image, (l + a, t + b), (a, b), 0, 0, 360,
			(0, 255, 0), 2)
	for l, t, w, h in noses:
		a, b = int(w / 2), int(h / 2)
		cv.ellipse(image, (l + a, t + b), (a, b), 0, 0, 360,
			(255, 0, 0), 2)
	cv.imshow('VideoCapture', image)
	if cv.waitKey(33) == 27:
		break
cap.release()
cv.destroyAllWindows()
