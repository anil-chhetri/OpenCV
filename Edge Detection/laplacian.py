import numpy as np
import cv2

'''
    Edge detection embodies mathematical methods to find points in 
    an image where the brightness of pixel intensities changes distinctly.
'''

## when computing gradients and edge we normally compute them on single channel
## hence grayscale.
image = cv2.imread('Images/coins.png', 0)

## In laplacian function 
#   first paramter is grayscale or single channel image
#   second parameter is data type of output image.
lap = cv2.Laplacian(image, cv2.CV_64F)

## this is done to include all the edges in the images as
## unsigned int doesn't provide value of negative number
lap = np.uint8(np.absolute(lap))


cv2.imshow('laplacian', lap)



cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()