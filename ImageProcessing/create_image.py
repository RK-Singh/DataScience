# /user/bin/python3

import numpy as np
import cv2

# utility function to display image
def imshow(filename, image):
	cv2.imshow(filename,image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

img = np.zeros((256, 256, 1), np.uint8)

intensity = 0
for i in range(256):
	img[i] = intensity
	intensity += 1

imshow('greyscale range', img)