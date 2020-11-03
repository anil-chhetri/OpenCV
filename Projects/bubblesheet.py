import cv2
import numpy as np

def order_points(points):
    rect = np.zeros((4,2), dtype='float32')
   
    s = np.sum(points, axis=1)
    rect[0] = points[np.argmin(s)]
    rect[2] = points[np.argmax(s)]
   
    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]
   
    return rect

def four_point_transform(image, points):
    rect = order_points(points)
    (tl, tr, br, bl) = rect
    
    widthA = np.sqrt( ((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2) )
    widthB = np.sqrt( ((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2) )
    maxWidth = max(int(widthA), int(widthB))
    
    heightA = np.sqrt( ((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2 ) )
    heightB = np.sqrt( ((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2 ) )
    maxHeight = max(int(heightA), int(heightB))
    
    dst = np.array([
        [0,0],
        [maxWidth -1, 0],
        [maxWidth - 1, maxHeight -1],
        [0, maxHeight - 1]
    ], dtype='float32')
    
    M = cv2.getPerspectiveTransform(rect, dst)
    
    wrapped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return wrapped

def sort_contours(contours, direction='left-to-right'):
    
    reverse = False
    index = 0
    
    if direction == 'right-to-left' or direction == 'bottom-to-top':
        reverse = True
        
    if direction == 'top-to-bottom' or direction == 'bottom-to-top':
        index = 1
        
    boundingBox = [cv2.boundingRect(c) for c in contours]
    (contours, boundingBox) = zip(*sorted(zip(contours, boundingBox)
                                          , key=lambda  b: b[1][index]
                                          , reverse=reverse))
    return contours, boundingBox


## step 1: detect image
image = cv2.imread(r'E:\practise\OpenCV\Images\bubblesheet.png')
ori = image.copy()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edge = cv2.Canny(blur, 75,200)

contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
docCnt = None

if len(contours) > 0:
    
    cnts = sorted(contours, key=cv2.contourArea, reverse=True)
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        
        if len(approx) == 4:
            docCnt = approx
            break


paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4,2))

ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}
# cv2.imshow('wraped', warped)


## apply ostu thresholding
t, thresh = cv2.threshold(warped, 0 ,255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)


#print(cv2.boundingRect(gray))

## find contours on thersold(binary image)
contours_thresh, hierarchy_thresh = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
questionCnts = []

for c in contours_thresh:
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)
    
    if w >= 20 and h >= 20 and ar >= 0.9 and ar<=1.1: 
        questionCnts.append(c)


questionCnts, boundingbox = sort_contours(questionCnts, direction="top-to-bottom")
correct = 0

for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):

    cnt = sort_contours(questionCnts[i:i+5], direction='left-to-right')[0]
    bubbled = None
    #cv2.drawContours(paper, cnt, -1, (np.random.randint(50,255), np.random.randint(50,255), np.random.randint(0,255)), 2)

    for (j, c) in enumerate(cnt):
        mask = np.zeros(thresh.shape, dtype='uint8')
        cv2.drawContours(mask, [c], -1, 255, -1)
    
        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)
        
        
        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)
            
    color = (0,0,255)
    k = ANSWER_KEY[q]

    if k ==  bubbled[1]:
        color = (0,255,0)
        correct += 1

    cv2.drawContours(paper, [cnt[k]], -1, color, thickness=3)
    
  
# cv2.imshow('Threshold image.', thresh)
cv2.imshow('paper', paper)
cv2.imshow('original', ori)
cv2.waitKey(0)
cv2.destroyAllWindows()