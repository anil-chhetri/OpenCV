import numpy as np
import cv2
import mahotas

''' 
    Another way to automatically compute of threshold 
    value of T is to use Otsu's Method.
'''

'''
Working:
    Otsu’s method assumes there are two peaks in the grayscale
    histogram of the image. It then tries to find an optimal
    value to separate these two peaks – thus our value of T.
'''

##using mahotas

# reading image as grayscale image.
image = cv2.imread('Images/coins.png', 0) # 0 or cv2.IMREAD_GRAYSCALE

blurred = cv2.GaussianBlur(image, (7,7), 0)

# compute global threshold using otsu method. 
T = mahotas.thresholding.otsu(blurred)
print('otsu threshold', T)

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('otsu image', thresh)


T = mahotas.thresholding.rc(blurred)

thresh = image.copy()
thresh[thresh >  T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow('Riddler-Calvered ', thresh)



## opencv method
thresh = image.copy()
Tvalue, thresh = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
print(Tvalue)
#thresh = cv2.bitwise_not(thresh)
cv2.imshow('ostu opencv', thresh)





 
 
 
cv2.imshow('image', blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
 


