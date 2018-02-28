import numpy as np
import cv2 as cv
with open('letter.dat', 'r') as f:
	for line in f.readlines():
		items = line.split('\t')
		char, image = items[1], items[6:-1]
		image = cv.resize(
			np.array(image, dtype=np.uint8).reshape(16, 8) * 255,
			None, fx=25, fy=25)
		cv.imshow(char, image)
		if cv.waitKey(100) == 27:
			break