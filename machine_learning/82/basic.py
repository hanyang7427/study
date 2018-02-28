import numpy as np
import cv2
original_image = cv2.imread('forest.jpg')
cv2.imshow('Original Image', original_image)
blue_image = original_image.copy()
blue_image[..., [1, 2]] = 0
cv2.imshow('Blue Image', blue_image)
green_image = original_image.copy()
green_image[..., [0, 2]] = 0
cv2.imshow('Green Image', green_image)
red_image = original_image.copy()
red_image[..., [0, 1]] = 0
cv2.imshow('Red Image', red_image)
h, w = original_image.shape[:-1]
l, t, r, b = int(w / 4), int(h / 4), int(w * 3 / 4), int(h * 3 / 4)
crop_image = original_image[t:b, l:r]
cv2.imshow('Crop Image', crop_image)
small_image = cv2.resize(original_image, (int(w / 8), int(h / 8)),
	interpolation=cv2.INTER_LINEAR)
cv2.imshow('Small Image', small_image)
cv2.imwrite('small.jpg', small_image)
big_image = cv2.resize(small_image, None, fx=8, fy=8,
	interpolation=cv2.INTER_AREA)
cv2.imshow('Big Image', big_image)
cv2.waitKey()
