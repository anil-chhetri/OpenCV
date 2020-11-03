import numpy as np
import cv2

image = cv2.imread(r'E:\practise\OpenCV\Images\shapes_and_colors.jpg')
##E:\practise\OpenCV\Images\shapes_and_colors.jpg

grayScale =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayScale, (11,11), 0)
tvalue, thresh = cv2.threshold(blurred, 60,255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

#cv2.drawContours(image, contours, -1, (0,255,0), 2)

for c in contours:
    ### Image Moment is a particular weighted average of image 
    # pixel intensities, with the help of which we can 
    # find some specific properties of an image, like radius, 
    # area, centroid etc.
    
    M = cv2.moments(c)
    # print('c', c)
    # print('m', M)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    
    cv2.drawContours(image, [c], -1, (0,255,0), 2)
    cv2.circle(image, (cx, cy), 7, (255,255,255), -1 )



#cv2.imshow('edge', thresh)
cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()