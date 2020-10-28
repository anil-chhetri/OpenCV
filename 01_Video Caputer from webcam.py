import cv2

cap = cv2.VideoCapture(0)

fourccCode = cv2.VideoWriter_fourcc(*'XVID')


## saving the ouput of camera
out = cv2.VideoWriter('output.mp4',  ## name of output file
                      fourccCode,  ## fourcc code 
                      20.0,  ## Number of frame per second
                      (640,480)) ## size of caputer




## reading height and width
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 


while cap.isOpened():
    ## read the frame.
    success, frame = cap.read()
    
    if success:
        
        out.write(frame)
        
        ## convert the frame to gray scale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        ## show to frame to the screen
        cv2.imshow('video webcam', gray)
        
        
        ## show the frame for 1 millisecond and when q is pressed break.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
