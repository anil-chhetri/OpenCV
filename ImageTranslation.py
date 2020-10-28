import numpy as np
import cv2
import Imutils

img = cv2.imread('Images/car.jpg')
cv2.imshow('Original', img)


tx, ty = (50,50)

M = np.float32([[1,0,-tx], [0,1,-ty]])

'''
The first argument is the image we
wish to shift and the second argument is our translation matrix M. 
Finally, we manually supply the dimensions (width
and height) of our image as the third argument.
'''
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('Shifted', shifted)


newimg = Imutils.transalte(img, 0 ,100)
cv2.imshow('newimage', newimg)


cv2.waitKey(0)
cv2.destroyAllWindows()