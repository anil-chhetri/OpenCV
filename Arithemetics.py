import numpy as np
import cv2
import Imutils

img = cv2.imread('Images/car.jpg')
img = Imutils.resize(img, 500)

cv2.imshow('Images original', img)

## adding 100 intensity to the image.
M = np.ones(img.shape, dtype='uint8') * 100
newImg = cv2.add(img, M)
cv2.imshow('Added image', newImg)

## subtracting 50 intensity to the image.
M = np.ones(img.shape, dtype="uint8") * 50
subImg = cv2.subtract(img, M)
cv2.imshow('subtract image', subImg)



## numpy addition
M = np.ones(img.shape, dtype='uint8') * 100
newImg = np.add(img, M)
cv2.imshow('Added image(Numpy)', newImg)



## numpy subtraction
M = np.ones(img.shape, dtype='uint8') * 50
newImg = np.subtract(img, M)
cv2.imshow('subtract image(Numpy)', newImg)


cv2.waitKey(0)
cv2.destroyAllWindows()