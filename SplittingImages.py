import numpy as np
import cv2

image = cv2.imread('Images/car.jpg')
cv2.imshow('original', image)

(Blue, Green, Red) = cv2.split(image)

cv2.imshow('Blue', Blue)
cv2.imshow('Red', Red)
cv2.imshow('Green', Green)
cv2.waitKey(0)

merged = cv2.merge([Blue, Green, Red])
cv2.imshow('mergerd ' , merged)

cv2.waitKey(0)
cv2.destroyAllWindows()