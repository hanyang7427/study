import numpy as np
import scipy.misc as sm
import sklearn.cluster as sc
import matplotlib.pyplot as mp
def compress_image(image, bpp):
	n_clusters = np.power(2, bpp)
	x = image.reshape((-1, 1))
	model = sc.KMeans(n_init=4, n_clusters=n_clusters,
		random_state=5)
	model.fit(x)
	y = model.labels_
	centers = model.cluster_centers_.squeeze()
	z = centers[y]
	return z.reshape(image.shape)
image_8bpp = sm.imread('flower.jpg', True).astype(np.uint8)
image_4bpp = compress_image(image_8bpp, 4)
image_2bpp = compress_image(image_8bpp, 2)
image_1bpp = compress_image(image_8bpp, 1)
mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
mp.subplot(221)
mp.title('8 bits/pixel', fontsize=16)
mp.axis('off')
mp.imshow(image_8bpp, cmap='gray')
mp.subplot(222)
mp.title('4 bits/pixel', fontsize=16)
mp.axis('off')
mp.imshow(image_4bpp, cmap='gray')
mp.subplot(223)
mp.title('2 bits/pixel', fontsize=16)
mp.axis('off')
mp.imshow(image_2bpp, cmap='gray')
mp.subplot(224)
mp.title('1 bits/pixel', fontsize=16)
mp.axis('off')
mp.imshow(image_1bpp, cmap='gray')
mp.tight_layout()
mp.show()




