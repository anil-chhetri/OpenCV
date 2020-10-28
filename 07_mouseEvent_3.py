import cv2
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x,  2]
        cv2.circle(img, (x, y), 3, color=(17,200,12), thickness=-1)
        colorImage = np.zeros((720,980,3), dtype=np.uint8)
        
        #print(colorImage.shape)
        #Fill color to new image
        colorImage[:] = [blue, green, red]
        
        cv2.imshow('color', colorImage)

#img = np.zero((512,5123), dtype=np.uint8)

img = cv2.imread('Images/5395.jpg')
img = cv2.resize(img, (980, 720))
print(img.shape)
cv2.imshow('Images', img)

cv2.setMouseCallback('Images', click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()