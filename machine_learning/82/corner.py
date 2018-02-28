import numpy as np
import cv2
original_image = cv2.imread('box.png')
cv2.imshow('Original Image', original_image)
gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray Image', gray_image)
corner = cv2.cornerHarris(gray_image, 7, 5, 0.04)
corner_image = cv2.dilate(corner, None)
cv2.imshow('Corner Image', corner_image)
threshold = corner_image.max() * 0.01
corner_max = corner_image > threshold
original_image[corner_max] = [0, 0, 255]
cv2.imshow('Detected Image', original_image)
cv2.waitKey()