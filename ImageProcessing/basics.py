# /usr/bin/python3

import numpy as np
import cv2

# utility function to display image
def imshow(filename, image):
	cv2.imshow(filename,image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# the filename of the image
filename = 'aquaman.png'

# reading the image file
image = cv2.imread(filename, cv2.IMREAD_COLOR)

# displayimg the image
imshow(filename,image)

# calculate the negative
negimage = 255 - image

# display negative
imshow('negative of ' + filename, negimage)

# write negative image
cv2.imwrite('negative.png',negimage)

# crop/segment a portion of the image
subimage = image[45:140, 375:465]

imshow('cropped image', subimage)

# placing the cropped image on another image
negimage[45:140, 375:465] = subimage

imshow('cropped image', negimage)
