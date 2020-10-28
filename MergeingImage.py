import numpy as np
import cv2

image = cv2.imread('Images/car.jpg')
cv2.imshow('original', image)

zeros = np.zeros(image.shape[:2], dtype='uint8')

(B, G, R) = cv2.split(image)

cv2.imshow('Red',cv2.merge([zeros,zeros, R ]))
cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))


cv2.waitKey(0)
cv2.destroyAllWindows()
