import numpy as np
import cv2
original_image = cv2.imread('chair.jpg')
cv2.imshow('Original Image', original_image)
hor_image = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow('Hor-Sobel Image', hor_image)
ver_image = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow('Ver-Sobel Image', ver_image)
all_image = cv2.Sobel(original_image, cv2.CV_64F, 1, 1, ksize=5)
cv2.imshow('All-Sobel Image', all_image)
lap_image = cv2.Laplacian(original_image, cv2.CV_64F)
cv2.imshow('Laplacian Image', lap_image)
can_image = cv2.Canny(original_image, 50, 240)
cv2.imshow('Laplacian Image', can_image)
cv2.waitKey()