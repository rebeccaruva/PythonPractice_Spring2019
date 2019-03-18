###############
#
# basic image operations
# ex: get region of image and change pixel colors
# show roi on diff part of image
#
# by bex
#
###############

import cv2
import numpy as np

img = cv2.imread('rm.jpg', cv2.IMREAD_COLOR) # source will usually remain in color

# img[300, 270] = [0, 255, 0] #convert that pixel to green
# px = img[300,270]
# print(px) # prints color value for that pixel

# # ROI stands for region of the image
# roi = img[100:150, 100:150]
# print(roi)

#img[y region, x region] ?? why
img[100:150, 100:150] = [255, 255, 255] # convert roi to white square

rm_face = img[100:400, 260:530] #region
img[0:300, 0:270] = rm_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
