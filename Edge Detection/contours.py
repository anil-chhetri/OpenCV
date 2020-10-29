import numpy as np
import cv2

'''
    Contour is a curve of points, with no gaps in the curve. 
    or Contours can be explained simply as a curve joining all the 
    continuous points (along boundary), having same color or intensity.
    
    Notes:
        >> for better accuracy, use binary images. apply threshold 
            or canny edge detection
        >> In opencv, finding contours is like fining white objects from black
            background. so object to be found should be white and background 
            should be black
'''

cimage = cv2.imread('Images/coins.png')
image = cv2.cvtColor(cimage, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (11,11), 0)

edge = cv2.Canny(blurred, 30,150)


## using contours
# The second argument is the type of contours we want.
# we use CV2.RETR_EXTERNAL to retrieve only the outermost contours
# we can also use cv2.RETR_LIST to grab all contours 
# Other method include hierarchical contours using cv2.RETR_COMP and cv2.RETR_TREE.

## Last argument is how we want to aprrorximate the contours. 
# we use cv2.CHAIN_APPROX_SIMMPLE  to compress horizontal, vertical
#  and diagonal segement into their endpoints only.
# if you want all the points along the contour, without compression 
#  cv2.CHAIN_APPROX_NONE is used. 

(contours, hierarchy) = cv2.findContours(edge.copy()
                                , cv2.RETR_EXTERNAL
                                , cv2.CHAIN_APPROX_SIMPLE)

print(f'I count {len(contours)} coins in the image.')


## drawing contours
## In drawContours function, 
#   first argument is the source image, 
#   second argument is the contours which should be passed as python list
#   third argument is index of contours (-1 to draw all)
#   and remaing are color and thickness
cv2.drawContours(cimage, contours, -1, (0,255,0), 3)


# cv2.imshow('image', image)
# cv2.imshow('canny', edge)
cv2.imshow('colored image', cimage)


for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)

    print('COIN #{}'.format(i+1))
    coin = image[y:y+h, x:x+w]
    cv2.imshow('coin', coin)


cv2.waitKey(0)
cv2.destroyAllWindows()
