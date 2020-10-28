import numpy as np
import cv2

image = cv2.imread('Images/car.jpg')
r = 500 / image.shape[0]
dim = (int(r * image.shape[1]), 500)
image = cv2.resize(image, dim) 

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayImage, (7,7), 0)

'''
Adaptive Thresholding algorithm determines the threshold for a pixel based  on 
a small region around it.  so we get different threshold value for different 
region of  images which give better results for images varying illumination.
'''

img = cv2.adaptiveThreshold(blurred, maxValue=255, 
                            adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            thresholdType=cv2.THRESH_BINARY,
                            blockSize=11,
                            C=3)

'''
The adaptive method decide how threshold value is calculated:
cv2.ADAPTIVE_THRESH_GAUSSIAN_C : The threshold value is a gaussian-weighted sum of the 
    neighbourhood values minus the constant C.
    
cv2.ADAPTIVE_THRESH_MEAN_C :  The threshold value is the mean of the 
    neighbourhood area minus the constant C.
    
The blockSize determines the size of the neighbourhood area(choose odd number).
'''

final = cv2.bitwise_and(image, image, mask=img)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()