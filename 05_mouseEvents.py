import cv2
import numpy as np



## list of all the events
# events = [x for x in dir(cv2) if 'EVENT' in x]
# print(events)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cordinate = str(x) + ' ' + str(y)
        print(cordinate)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, cordinate, (x, y), font, .5, color=(0,255,0), thickness=1)
        cv2.imshow('Image', img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x, 0]
        green = img[y, x, 1]
        red = img[y, x , 2]
        bgr = str(blue)+','+str(green)+','+str(red)
        print(bgr)
        cv2.putText(img, bgr, (x, y), cv2.FONT_HERSHEY_DUPLEX, .5, color=(0,255,255), thickness = 1)
        cv2.imshow('Image', img)
        
        
        
        

img = np.zeros((512,512,3), dtype=np.uint8)
#cv2.imshow('Image', img)
img = cv2.imread('Images/331995.jpg')
cv2.imshow('Image', img)



#calling events 
## Note:: windows name should be same
cv2.setMouseCallback('Image', click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()