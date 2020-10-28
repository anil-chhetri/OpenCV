import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass
## creating track bar

cv2.namedWindow('trackbar')

cv2.createTrackbar('lowerH', 'trackbar', 0, 360, nothing)
cv2.createTrackbar('higherH', 'trackbar', 0, 360, nothing)

cv2.createTrackbar('lowerS', 'trackbar', 0, 100, nothing)
cv2.createTrackbar('higherS', 'trackbar', 0, 100, nothing)

cv2.createTrackbar('lowerV', 'trackbar', 0, 100, nothing)
cv2.createTrackbar('higherV', 'trackbar', 0, 100, nothing)

blank = np.zeros((512,512,3))

while True:
    
    success, frame = cap.read()
    
    if success:
        
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        higherH = cv2.getTrackbarPos('higherH', 'trackbar')
        lowerH = cv2.getTrackbarPos('lowerH', 'trackbar')
        
        higherV = cv2.getTrackbarPos('higherV', 'trackbar')
        lowerV = cv2.getTrackbarPos('lowerV', 'trackbar')
        
        higherS = cv2.getTrackbarPos('higherS', 'trackbar')
        lowerS = cv2.getTrackbarPos('lowerS', 'trackbar')
        
        #print(np.array([lowerH, lowerS, lowerV]))
        #print(np.array([higherH, higherS, higherV]))
        
        mask = cv2.inRange(hsv_image, 
                           np.array([lowerH, lowerS, lowerV]), 
                           np.array([higherH, higherS, higherV]))
        
        
        res = cv2.bitwise_and(frame, frame, mask=mask)
        
        
        cv2.imshow('camera', frame)
        #cv2.imshow('hsv_image', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('result', res)
        
        #cv2.imshow('trackbar')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     
     
        
cap.release()
cv2.destroyAllWindows()