import cv2
import datetime

cap = cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

cap.set(3, 1280)
cap.set(4, 720)





while cap.isOpened():
    
    success, frame = cap.read()
    
    if success:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        text = 'Width : ' + str(cap.get(3)) + ' Height : ' + str(cap.get(4))


        datestr = str(datetime.datetime.now())
        
        ## keeping width and height
        frame = cv2.putText(frame,  text, (1-0,50), font, 1, color=(255,0,0), thickness=2)
        
        ## keeping time and date
        frame = cv2.putText(frame, datestr, (800, 50), fontFace=font, fontScale=1, color=(0,255,0),thickness=2)
        
        ## showing frame.
        cv2.imshow('writing to screen', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
