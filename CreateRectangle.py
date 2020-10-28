import cv2
import numpy as np

## right click for color change and left click and drag for drawing.

np.random.seed(52)
blankImage = np.zeros((512,512,3), dtype=np.uint8)

lbuttonDownFlag , x1, y1, fcolor = False, 0,0, (255,0,0)


def click_event(event, x, y, flags, params):
    global lbuttonDownFlag, x1, y1, fcolor
    if event == cv2.EVENT_LBUTTONDOWN:
        
        lbuttonDownFlag = True
        x1 = x
        y1 = y
       # print(lbuttonDownFlag, x1, y1)
        
        #cv2.circle(blankImage, (x, y), 40, (0,255,0), -1)
        
    if event == cv2.EVENT_MOUSEMOVE:
        if lbuttonDownFlag : 
            print('painting', fcolor)
            cv2.rectangle(blankImage, (x1, y1) ,(x, y), fcolor, thickness=-1)
        
            
    if event == cv2.EVENT_LBUTTONUP:
        lbuttonDownFlag = False
        #print('mouse up ', lbuttonDownFlag)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        
        blue = np.random.randint(0,255)
        green = np.random.randint(0,255)
        red = np.random.randint(0,255)
        fcolor = (blue, green, red)
        print('color change', fcolor)
        
        


while True: 
    cv2.imshow('image', blankImage) 
    cv2.setMouseCallback('image', click_event) 
    if cv2.waitKey(1) == 27:
        break
    
    

 

#cv2.waitKey(0)
cv2.destroyAllWindows()