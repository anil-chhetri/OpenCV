import cv2

# class FaceDetector:
    
#     def __init__(self, faceCascadePath):
#         self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        
    
#     def detect(self, Image, scaleFactor=1.1, minNeighbour=5, minSize=(30,30)):
#         rect = self.faceCascade.detectMultiScale(image, 
#                                                  scaleFactor=scaleFactor,
#                                                  minNeighbors=minNeighbour, 
#                                                  minSize=minSize)
        
#         return rect
    
    
#fd = FaceDetector('./cascades/haarcascade_frontalface_default.xml')
image = cv2.imread('E:\\practise\\OpenCV\\Images\\messi2.png')

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('image', grayscale)
fd = cv2.CascadeClassifier('E:/practise/OpenCV/Projects/cascades/haarcascade_frontalface_default.xml')

facerect = fd.detectMultiScale(grayscale, scaleFactor=1.1
                               , minNeighbors=15
                               , flags= cv2.CASCADE_FIND_BIGGEST_OBJECT
)

for (x, y, w, h) in facerect:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()