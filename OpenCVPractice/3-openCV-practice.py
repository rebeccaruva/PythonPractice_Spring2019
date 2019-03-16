###############
#
# read imageand add shapes
# possible shapes: line, circle, rect, polygon, font
# can color, change width, change size, use anti-aliasing if needed
#
# by bex
#
###############

import cv2
import numpy as np

img = cv2.imread('rm.jpg', cv2.IMREAD_COLOR) # read image in with color
cv2.line(img, (0,0), (400, 300), (255, 0, 0), 15, cv2.LINE_AA) #draw line on image, start and end point, and color (BGR) of line, and width

cv2.rectangle(img, (15, 25), (200, 150), (255, 255, 255), 5) #draw rect on image, start/end point, color, and width

cv2.circle(img, (450, 200), 55, (0, 0, 255), -1) #draw circle in img, center, radius, color, and width or -1 for fill

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32) # array of points for polygon (2 by 1 array)
# pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 0), 4) #polygon on image, from points list, true or false: final point connect to first point, color, width

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV yeahhh', (300, 250), font, 2, (255, 150, 50), 2, cv2.LINE_AA) # put text on img, string to put, bottom left point, font, size, color, thickness, anti-aliasing

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
