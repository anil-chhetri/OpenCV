import numpy as np
import cv2


def transalte(image, x, y):
    M = np.float32([[1,0,x], [0,1,y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image, angle, center=None, scale=1):
    (h, w) = image.shape[:2]
    
    if center is None:
        center = (w//2, h//2)
        
    M = cv2.getRotationMatrix2D(center, angle, scale)
    roated = cv2.warpAffine(image, M, (w, h))
    return roated


def resize(image, width=None, height=None, interpolation=cv2.INTER_AREA):
    
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / image.shape[0]
        dim = (int(image.shape[1] * r), height)
        
    if height is None:
        r = width / image.shape[1]
        dim = (width, int(image.shape[0] * r))
        
    resized = cv2.resize(image, dim, interpolation=interpolation)
    print(resized.shape)
    
    return resized
    
    
def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cx, cy) = ( w // 2, h // 2)
    
    M = cv2.getRotationMatrix2D((cx, cy), -angle, 1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])
    
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    
    M[0,2] += (nW / 2) - cX
    M[1,2] += (nH / 2) - cy
    
    return cv2.warpAffine(image, M, (nW, nH))