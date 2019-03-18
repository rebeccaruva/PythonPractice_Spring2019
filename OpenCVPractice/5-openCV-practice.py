###############
#
# simple image arithmetics
# logical operations
# ex: adding images together, superimposing
#
# by bex
#
###############

import cv2
import numpy as np

# the two images have to be the SAME SIZE !!
img1 = cv2.imread('dog1.jpg')
img2 = cv2.imread('dog2.jpg')

img3 =  cv2.imread('guideDogsLogo.jpg')
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols] #define roi for img1 based on img3 size

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
# threshold: if pixel value is above 220, itll be converted to 255 (white). if below 220, convert to black, either 0 or 1 threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# bitwise is a lowlevel logical operation, just like more in depth python logical operation
mask_inv = cv2.bitwise_not(mask)
# ex: bitwise_and, bitwise_or, bitwise_not, bitwise_xor (only 1)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) #if put mask here, white will show
img3_fg = cv2.bitwise_and(img3, img3, mask=mask) #along with mask_inv here (white will show)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

# add = img1 + img2 #not ideal

#add = cv2.add(img1, img2) # added pixel values together
# example of adding two pixel values together:
# (155, 211, 79) + (50, 170, 200) = 205, 381, 279... translated to (205, 255, 255)
# ^^which is why the image looks bright white

# add image and impose over each other
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) #values: img1, weight of 1, img2, weight of 2, gamma (leave alone)

cv2.imshow('res', img1)
# cv2.imshow('mask_inv', mask_inv)
# cv2.imshow('img1_bg', img1_bg)
# cv2.imshow('img3_fg', img3_fg)
# cv2.imshow('dst', dst)

#cv2.imshow('gray', img2gray)

#cv2.imshow('mask', mask)

# cv2.imshow('add', add)
# cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
