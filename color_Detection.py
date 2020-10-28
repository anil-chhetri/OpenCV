import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('Images/car.jpg')
cv2.namedWindow('HSV')

cv2.createTrackbar('highH', 'HSV', 183, 255, nothing)
cv2.createTrackbar('lowH', 'HSV', 35, 179, nothing)

cv2.createTrackbar('highS', 'HSV', 255, 255, nothing)
cv2.createTrackbar('lowS', 'HSV', 0, 255, nothing)

cv2.createTrackbar('highV', 'HSV', 216, 255, nothing)
cv2.createTrackbar('lowV', 'HSV', 0, 255, nothing)

while True:
    
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    highH = cv2.getTrackbarPos('highH', 'HSV')
    lowH = cv2.getTrackbarPos('lowH', 'HSV')
    
    highS = cv2.getTrackbarPos('highS', 'HSV')
    lowS = cv2.getTrackbarPos('lowS', 'HSV')
    
    highV = cv2.getTrackbarPos('highV', 'HSV')
    lowV = cv2.getTrackbarPos('lowV', 'HSV')
    
    low = np.array([lowH, lowS, lowV])
    high = np.array([highH, highS, highV])
    
    print(low, high)
    
    mask = cv2.inRange(img_hsv, low, high)
    
    res = cv2.bitwise_and(img, img, mask=mask)
       
    
    cv2.imshow('car', img)
    cv2.imshow('hsv', mask)
    cv2.imshow('result', res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cv2.destroyAllWindows()
