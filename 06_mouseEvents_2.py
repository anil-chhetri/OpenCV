import cv2


def click_event(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0,212,63), -1)
        points.append((x, y))
        #print(points)
        
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], color=(255,255,255), thickness=1)
        
        cv2.imshow('Image', img)




img = cv2.imread('Images/331995.jpg')
cv2.imshow('Image', img)

points = []

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()