import cv2
import numpy as np


def nothing(x):
    pass

#img = np.zeros((512,512,3), dtype=np.uint8)

cv2.namedWindow('image')


cv2.createTrackbar('CP', 'image', 10,400, nothing)


cv2.createTrackbar('color', 'image', 0,1, nothing)

while True:
    
    img = cv2.imread('Images/5395.jpg')
    img = cv2.resize(img, (512,512))
    
    
    pos = cv2.getTrackbarPos('CP', 'image')
    
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, str(pos), (50,100), font, 2, (0,210,255))
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    s = cv2.getTrackbarPos('color', 'image')
    
    
    if s == 0:
        pass
        
    else:
       img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       
    cv2.imshow('image', img)
    
cv2.destroyAllWindows()