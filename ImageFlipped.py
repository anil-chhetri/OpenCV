import numpy as np
import cv2
import Imutils as i

img = cv2.imread('Images/car.jpg')


img = i.resize(img, width=500)
cv2.imshow('original', img)

hflipped = cv2.flip(img, 1)
cv2.imshow('Horizontally flipped', hflipped) 

vflipped = cv2.flip(img, 0)
cv2.imshow('vertical flipped', vflipped)

flipped = cv2.flip(img, -1)
cv2.imshow('horizontally and vertically', flipped)


if cv2.waitKey(0) == 'q':
    cv2.destroyAllWindows()
