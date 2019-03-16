###############
#
# take in video from webcam
# modify video from webcam live
# write video out to saved file
#
# by bex
#
###############

import cv2
import numpy as np

#  capture the first webcam in your system
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #add codec to then save video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) #save video as output, fourcc codec, 20 fps, and size

while True:
    ret, frame = cap.read() #return is true or false, and then you'll get frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grey color
    out.write(frame) #write color frame to save video
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey (1) & 0xFF == ord('q'): #if key pressed and key is q
        break #break look

cap.release() #release capture (camera will be released)
out.release() #stop save video
cv2.destroyAllWindows()
