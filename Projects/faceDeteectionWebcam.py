import cv2

cap = cv2.VideoCapture(0)

fd = cv2.CascadeClassifier('E:/practise/OpenCV/Projects/cascades/haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('E:\practise\OpenCV\Projects\cascades\haarcascade_eye.xml')


while cap.isOpened():
    
    success, frame = cap.read()
    
    if success:
        
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        eyerect = eye.detectMultiScale(grayframe, 1.05, 15)
    
        
        for (x, y, h, w) in eyerect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        
        # for (x, y, h, w) in smilerect:
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        
        rect = fd.detectMultiScale(grayframe, 1.1, 15)
        for (x, y, h, w) in rect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            
        cv2.imshow('setting paramter', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
    
    