import numpy as np
import cv2

'''
    Canny Edge Detector is a multi-step process. It involves blurring 
    the image to remove noise, computing Sobel gradient images in 
    x and y direction, suppressing edges, and finally a hysteresis thresholding
    stage that detemines if a pixel is 'edge-like' or not.
'''


image = cv2.imread('Images/coins.png', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5,5), 0)

## Argument of Canny function are 
#   first: blurred grayscale image
#   Second and third are threshold1 and threshold2
#       any gradient value larger than threshold2 is considered to be 
#       edge. Any value below threshold1 is considered not to be an edge
#       values in between threshold1 and thershold2 are either classified as
#       edge or non-edges based on how their intensities are "connected"
# 
# In below example any gradient value below 30 are considered non-edge whereas
# any values above 150 are considered edges..

canny = cv2.Canny(image, 30, 150)
bcanny = cv2.Canny(blurred, 40, 150)

canny_h = np.hstack([canny, bcanny])

cv2.imshow('Image', blurred)
cv2.imshow('canny', canny_h)


cv2.waitKey(0)
cv2.destroyAllWindows()