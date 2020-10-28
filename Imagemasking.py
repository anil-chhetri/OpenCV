import numpy as np
import cv2

img = cv2.imread('Images/car.jpg')
cv2.imshow('original', img)
#print(img.shape)

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (120,210), (830,550), (255,255,255), thickness=-1)
#cv2.imshow('mask', mask)

print(img.shape, mask.shape)

masked = cv2.bitwise_or(img, img, mask=mask)
cv2.imshow('masked', masked)


circularMask = np.zeros(img.shape[:2], dtype='uint8')
cv2.circle(circularMask, (img.shape[1]//2, img.shape[0]//2), 300, 255, thickness=-1)
circularMask = cv2.bitwise_and(img, img, mask=circularMask)
cv2.imshow('circluar mask', circularMask)

cv2.waitKey(0)
cv2.destroyAllWindows()
