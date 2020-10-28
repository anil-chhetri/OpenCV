import cv2

img = cv2.imread('Images/5395.jpg')
img = cv2.resize(img, (600,480))


#drawing line
img = cv2.line(img,  ## images
               (0,0),  #start point
               (255,255), #end point
               color=(147,96,44), ## in the format of BGR
               thickness=5
               )


img = cv2.arrowedLine(img,
                      (10,255),
                      (255,255), 
                      color=(255,0,0),
                      thickness=5)



img = cv2.rectangle(img, 
                    (384,0), 
                    (300,240),
                    (255,0,255),
                    thickness=-1)


img = cv2.putText(img, 'OpenCV', (0, 384), cv2.FONT_HERSHEY_DUPLEX, 2, (0,255,255), cv2.LINE_4)


cv2.imshow('drawing Geometric Shape', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
