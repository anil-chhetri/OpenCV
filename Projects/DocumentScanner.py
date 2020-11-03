import cv2
import numpy as np

from skimage.filters import threshold_local
# threshold_local function helps us obtain the black 
# and white feel to our scanned image.


def  order_points(points):
    '''
        It is absolutely crucial that we have consistent ordering of the points
        in the rectangle. The actual ordering itself can be arbitrary as long 
        as it is consistent throughout the implementation.
        
        top-left, top-right, bottom-right, bottom-left order.
    '''
    
    
    # Initialize a list of coordinates that will be ordered 
    # such that the first entry in the list is the top-left
    # , the second entry is top-right, the third is the 
    #  bottom-right and the fourth is the bottom-left
    
    rect = np.zeros((4,2), dtype='float32')
    
    ## the top left point will be the smallesst sum, whereas
    # the bottom-right point will have the largest sum
    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]
    rect[2] = points[np.argmax(s)]
    
    
    ## now compute the differece between the points, the 
    # top-right point will have te smallest difference, 
    # whereas the bottom-left will have the largest difference
    
    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]
    
    return rect


def four_point_transfrom(image, points):
    ## obtain a consistent order of the points and upackk them individually
    rect = order_points(points)
    (tl, tr, br, bl) = rect
    
    ### compute the width of the new image, which will be the maximum 
    # distance between bottom-right and bottom-left  x-coordinate or the 
    # top-right and top-left x-coordinates
    
    widthA = np.sqrt( ((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2) )
    widthB = np.sqrt( ((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2) )
    maxWidth = max(int(widthA), int(widthB))
    
    
    ## compute the height of the new image, which will be the maximum 
    # distance between the top-right and bottom-right y-coordinate or 
    # the top-left and bottom-left y-coordinate.
    
    heightA = np.sqrt( ((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2 ) )
    heightB = np.sqrt( ((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2 ) )
    maxHeight = max(int(heightA), int(heightB))
    
    
    ## now that we have the dimensions of the new image, construct the 
    # set of destination points to obtain a "bird eye view", ie(top-down view) 
    # of the image, again specifying points in the top-left, top-right
    # , bottom-right, and bottom-left order
    
    dst = np.array([
        [0,0],
        [maxWidth -1, 0],
        [maxWidth - 1, maxHeight -1],
        [0, maxHeight - 1]
    ], dtype='float32')
    
    '''
        we define 4 points representing our “top-down” view of the image. 
        The first entry in the list is (0, 0)  indicating the top-left corner. 
        The second entry is (maxWidth - 1, 0)  which corresponds to the 
        top-right corner. Then we have (maxWidth - 1, maxHeight - 1)  
        which is the bottom-right corner. 
        Finally, we have (0, maxHeight - 1)  which is the bottom-left corner.
    '''
           
    M = cv2.getPerspectiveTransform(rect, dst)
    '''
        To actually obtain the top-down, “birds eye view” of the image we’ll 
        utilize the cv2.getPerspectiveTransform  function. This function 
        requires two arguments, rect , which is the list of 4 ROI points 
        in the original image, and dst , which is our list of transformed points.
        The cv2.getPerspectiveTransform  function returns M , 
        which is the actual transformation matrix.
    '''
    
    wrapped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return wrapped


def resize(image, height=None, width=None, scale=1.0):
    
    if height is None and width is None:
        return image
    
    if width is None:
        ratio = height / image.shape[0]
        dim = (height , int(image.shape[1] * ratio))
       # image = cv2.resize(image, (height, image.shape[1] * ratio), interpolation=cv2.INTER_AREA)
        
    if height is None:
        ratio = width / image.shape[1]
        dim = (int(image.shape[1] * ratio), width)
        #image = cv2.resize(image, (image.shape[0] * ratio, width),interpolation=cv2.INTER_AREA)
        
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image

### Step 1: Edge Detection

# load the image and compute the ratio of the old height 
# to the new height, clone it, and resize it

image = cv2.imread('E:\practise\OpenCV\Images\scanned.png')
ratio = image.shape[0] / 1000.0
orig = image.copy()
#image= resize(image, height=200)


## convert the image to grayscale, blur it, and find edges 
# in the images
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurr = cv2.GaussianBlur(image, (3,3), 0) ## remove high frequency noise
edge = cv2.Canny(blurr, 10, 100)


## show the original image and the edge deted image
cv2.imshow('Image', image)
cv2.imshow('edge', edge)



### step 2 : Finding contours

## find the contours in the edged image, keeping only 
# the largest ones, and initalize the screen contours
contours, heirarchy = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) 
#cnts = len(contours)
cnts = sorted(contours, key=cv2.contourArea, reverse=True)


for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
    #if our approximated contour has four points, then we 
    # can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break
    
cv2.drawContours(image, cnts, 0, (0,225,0), 2)
cv2.imshow('outline', image)

print(screenCnt.reshape(4,2))
### step 3 apply a perspective transform and thereshold

wraped = four_point_transfrom(orig, screenCnt.reshape(4,2))

wraped = cv2.cvtColor(wraped, cv2.COLOR_BGR2GRAY)
T = threshold_local(wraped, 11, offset=10, method = 'gaussian')
wraped = (wraped > T).astype('uint8') * 255


#cv2.imshow('original', image)
cv2.imshow('final', wraped)

cv2.waitKey(0)
cv2.destroyAllWindows()


    
    
    

