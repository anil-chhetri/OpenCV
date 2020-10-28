import numpy as np
import cv2 

''' Thresolding is the binarization of an Image. we seek to convert
a grayscale image to a binary image, where the pixel are either 0 or 255.
'''

'''
A simple thresholding would be selecting a pixel value p, and then setting 
all pixel intensities less than p to zero, and all pixel values greater than 
p to 255. In this way we are able to create a binary representation of the image.
'''

image = cv2.imread('Images/car.jpg')

#converting image to grayscale for thresholding.
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Applying Gaussian blurring helps remove some of 
# the high frequency edges in the image(that we are not concerned with).
blurred = cv2.GaussianBlur(image, (5,5), 0)

(Tq, thresh) = cv2.threshold(blurred, 115, 255, cv2.THRESH_BINARY)

(Tq, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)


cv2.imshow('threshold', thresh)
cv2.imshow('thresholdInv', threshInv)
cv2.imshow('Image', image)




cv2.waitKey(0)
cv2.destroyAllWindows()