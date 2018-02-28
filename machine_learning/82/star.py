import numpy as np
import cv2
original_image = cv2.imread('table.jpg')
cv2.imshow('Original Image', original_image)
detector = cv2.xfeatures2d.StarDetector_create()
keypoints = detector.detect(original_image, None)
sift_image = original_image.copy()
cv2.drawKeypoints(original_image, keypoints, sift_image,
	flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Star Image', sift_image)
cv2.waitKey()