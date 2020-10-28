import cv2
import numpy as np


img = np.zeros((512,512,3), dtype=np.uint8)
cv2.namedWindow('image')

def nothing(x):
    print(x)
    

cv2.createTrackbar('B','image', 0, 255, nothing)
cv2.createTrackbar('G','image', 0, 255, nothing)
cv2.createTrackbar('R','image', 0, 255, nothing)

while True:
    
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    
    img[:] = [b, g, r]
    
    
cv2.destroyAllWindows()
    