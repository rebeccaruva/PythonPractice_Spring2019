###############
#
# take in an image, change color, and display
# plot over image with matplotlib
# save modified image
#
# by bex
#
###############

import cv2
import numpy as np
import matplotlib.pyplot as plt

#
# define image and read the image with imread
#
img = cv2.imread('rm.jpg', cv2.IMREAD_GRAYSCALE) #grayscale = number 0
# IMREAD_COLOR = number 1
# IMREAD_UNCHANGED = number -1

#
# show image with cv2:
# opencv does BGRA for color
#
cv2.imshow('image', img) # title image and then show img
cv2.waitKey(0) # waits for any key to be pressed
cv2.destroyAllWindows()

#
# show image with matplotlib
# matplotlib does RGBA for color
#
# #plt.imshow(img, cmap='gray', interpolation='bicubic')
# after show image, you can plot a line in cyan color on top of it
# #plt.plot([50, 100], [200, 400], 'c', linewidth=5)
# #plt.show()

#
# write image to save it
#
cv2.imwrite('rm-gray.jpg', img)
