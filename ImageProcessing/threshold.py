# /usr/bin/python3
import numpy as np
import cv2


# utility function to display image
def imshow(filename, image):
	cv2.imshow(filename,image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


img = cv2.imread('highway.png')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

sensitivity = 15
lower_green = np.array([15 - sensitivity,10,50])
upper_green = np.array([15 + sensitivity,105,170])

# Threshold the HSV image to get only grey colors
mask = cv2.inRange(img_hsv, lower_green, upper_green)

imshow('image', img)
imshow('mask', mask)