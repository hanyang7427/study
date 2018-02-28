import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while True:
	image = cap.read()[1]
	image = cv.resize(image, None, fx=0.75, fy=0.75,
		interpolation=cv.INTER_AREA)
	cv.imshow('VideoCapture', image)
	if cv.waitKey(33) == 27:
		break
cap.release()
cv.destroyAllWindows()
