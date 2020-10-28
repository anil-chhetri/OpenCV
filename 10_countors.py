import cv2
import numpy as np

img = cv2.imread('Images/1.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)

img_canny = cv2.Canny(img_blur, 50, 50)

cv2.imshow('original image',img)
cv2.imshow('gray', img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()