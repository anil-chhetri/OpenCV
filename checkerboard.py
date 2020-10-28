import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")

# loop over the image in 10 pixel blocks
for (row, y) in enumerate(range(0, 300, 20)):
	for (col, x) in enumerate(range(0, 300, 20)):
		# initialize the color as red
		color = (0, 0, 255)

		# check to see if BOTH the row and column are
		# even or odd, and if so, update the background
		# color
		if row % 2 == col % 2:
			color = (0, 0, 0)

		# draw a 10x10 rectangle
		cv2.rectangle(canvas, (x, y), (x + 20, y + 20),
			color, -1)
  
  
cv2.imshow('canvas', canvas)  
cv2.waitKey(0)
cv2.destroyAllWindows()
