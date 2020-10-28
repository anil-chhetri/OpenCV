import numpy as np
import cv2
import Imutils

img = cv2.imread('Images/car.jpg')

cv2.imshow('original', img)

(rows, cols) = img.shape[0], img.shape[1]
'''
The cv2.getRotationMatrix2D function takes three arguments: 
the point at which we want to rotate the image
around (in this case, the center of the image). We then
specify θ, the number of degrees we are going to rotate the
image by. The last argument is the scale of the image.
'''

M = cv2.getRotationMatrix2D((cols // 3, rows // 3), 45, scale=1)
rotated  = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotated', rotated)


cv2.imshow('ratated new', Imutils.rotate(img, 45))


cv2.waitKey(0)
cv2.destroyAllWindows()