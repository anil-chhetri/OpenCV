import numpy as np
import cv2
'''
    Sobel operators is a joint Gausssian smoothing plus 
    differentiation operation, so it is more resistant to noise.
'''


image  = cv2.imread('Images/coins.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('original', image)

## In cv2.Sobel function 
#   first argument is grayscale image, 
#   Second argument is output data type
#   Third and fourth argument are order of the derivatives in the 
#       x and y direction (specify the value of 1 and o to find vertical edge like regions
#        and 1 and 0 to find horizontal edge like region.) 
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0) ## vertical edge
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1) ## horizontal edge

## perform so that we dont lose any edges while casting the data types.
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)


cv2.imshow('sobel x', sobelX)
cv2.imshow('sobel y', sobelY)
cv2.imshow('combined ', sobelCombined)



cv2.waitKey(0)
cv2.destroyAllWindows()