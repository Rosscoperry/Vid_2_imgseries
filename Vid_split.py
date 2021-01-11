
"""
Created on Mon Jan 11 21:45:51 2020
"""

import cv2
vidcap = cv2.VideoCapture('755_759.avi')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.bmp" % count, image)     # save frame as BMP file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1