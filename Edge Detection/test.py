import numpy as np
import cv2

image = cv2.imread('Images/pills.png')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayimage, (5,5), 0)

edge = cv2.Canny(blurred, 10,200)
edge1 = cv2.Canny(blurred, 240,250)
edge3 = cv2.Canny(blurred, 200,250)

edges = np.hstack([edge, edge1, edge3])

cv2.imshow('image', image)
cv2.imshow('canny', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()