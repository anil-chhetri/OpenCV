import cv2


cap = cv2.VideoCapture(0)


## getting property of camera properties.
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


## setting property of camera:
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1980)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)



## getting changed value
cap.get(3) ## for width
cap.get(4) ## for height



while cap.isOpened():
    
    success, frame = cap.read()
    
    
    if success:
        
        cv2.imshow('setting paramter', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destoryAllWindows()