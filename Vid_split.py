
"""
Created on Mon Jan 11 21:45:51 2020
"""

import cv2
filename = '' #enter the video filename here -check destination
vidcap = cv2.VideoCapture(filename)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.bmp" % count, image)     # save frame as BMP file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
