import numpy as np
import cv2
import Imutils

rectangle = np.zeros((500,500), dtype='uint8')
rectangle = cv2.rectangle(rectangle, (20,20), (480,480), (255,255,255), -1)
cv2.imshow('rectangle', rectangle)

circle = np.zeros((500,500), dtype='uint8')
circle = cv2.circle(circle, (250,250), 245, 255, -1)
cv2.imshow('circle', circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow('bitwise - and', bitwiseAnd)


bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow('bitwise - or', bitwiseOr)


bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow('bitwise - not', bitwiseNot)

cv2.waitKey(0)
cv2.destroyAllWindows()