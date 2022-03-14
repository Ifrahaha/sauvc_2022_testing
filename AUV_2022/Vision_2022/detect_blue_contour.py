import cv2
import numpy as np

def biggestContourI(contours):
    maxVal = 0
    maxI = None
    for i in range(0, len(contours) - 1):
        if len(contours[i]) > maxVal:
            cs = contours[i]
            maxVal = len(contours[i])
            maxI = i
    return maxI
            
cam = cv2.VideoCapture(0)

while True:
    ret_val, img = cam.read()

    lower = np.array([154, 112, 47], dtype = "uint8")
    higher = np.array([212, 223, 146], dtype = "uint8")
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, w = img.shape[:2]
    flt = cv2.inRange(hsv, lower, higher);
    
    contours0, hierarchy = cv2.findContours(flt, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Only draw the biggest one
    bc = biggestContourI(contours0)
    cv2.drawContours(img,contours0, bc, (0,255,0), 3)
    
    cv2.imshow('my webcam', img)
    cv2.imshow('flt', flt)
    
    if cv2.waitKey(1) == 27:
        break  
cv2.destroyAllWindows()