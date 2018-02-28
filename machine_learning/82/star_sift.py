import numpy as np
import cv2
import matplotlib.pyplot as mp
original_image = cv2.imread('table.jpg')
cv2.imshow('Original Image', original_image)
detector = cv2.xfeatures2d.StarDetector_create()
keypoints = detector.detect(original_image, None)
detector = cv2.xfeatures2d.SIFT_create()
print(len(keypoints))
keypoints, desc = detector.compute(original_image, keypoints)
print(len(keypoints), desc.shape)
sift_image = original_image.copy()
cv2.drawKeypoints(original_image, keypoints, sift_image,
	flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Star-SIFT Image', sift_image)
mp.matshow(desc, cmap='jet')
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.title('Description', fontsize=20)
mp.xlabel('Feature', fontsize=14)
mp.ylabel('Sample', fontsize=14)
mp.tick_params(labelsize=10)
mp.show()