import numpy as np
import cv2
original_image = cv2.imread('sunrise.jpg')
cv2.imshow('Original Image', original_image)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)
equal_image = cv2.equalizeHist(gray_image)
cv2.imshow('Equal Image', equal_image)
yuv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2YUV)
yuv_image[..., 0] = cv2.equalizeHist(yuv_image[..., 0])
bgr_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
cv2.imshow('Color Image', bgr_image)
cv2.waitKey()