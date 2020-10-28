import numpy as np
import cv2


canvas = np.zeros((300,300,3), dtype = 'uint8')
center = canvas.shape[0] // 2, canvas.shape[1] // 2

for r in range(10,150, 25):
    cv2.circle(canvas, center, r, (255,255,255))

cv2.imshow('canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

