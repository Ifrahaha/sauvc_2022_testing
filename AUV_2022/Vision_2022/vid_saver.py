#!/usr/bin/env python
import sys
#sys.path.insert(0, '/home/crossfire/Programming projects/auv_testing/AUV2k19/motion')
#import movement
import cv2
import numpy as np
import time

######################################################

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_image = cv2.VideoWriter('recording-%s.mkv' % time.time(), fourcc, 20.0, (640, 480))

    
def main():
    while True:
        rec, image = cap.read()
        #cv2.imshow("Mask", cv2.resize(image, (640, 480)))
        key = cv2.waitKey(20)
        if key & 0xFF == ord('q'):
            tearDown()
            break

if __name__ == '__main__':
    main()
