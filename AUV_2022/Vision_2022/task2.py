#checking if prev contour is greater or smaller than current contour
#updated in task_2_final

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
            

def checkContour(contours):
    cont=[]
    maxVal = 0
    maxI = None
    for i in range(0, len(contours) - 1):
        if len(contours[i]) > maxVal:
            cs = contours[i]
            maxVal = len(contours[i])
            maxI = i
            bc = maxI
            cont.append(maxI)
    try:
        for i in range(len(cont)):
            
            if cont[i-1]>cont[i]:
                print("hold")
                if max(cont)>bc:
                    print("bc forward")
                #m.forward(100)
                    pass
                else:
                    break
                pass
                
                #m.hold()
            elif cont[i-1]<cont[i]:
                print("right")
                pass
                
                #m.right(100)
            elif cont[i-1]==cont[i]:
                print("right")
                if max(cont)>bc:
                    print("bc forward")
                #m.forward(100)
                    pass
                else:
                    break
        #m.hold()
                pass
                
                #m.right(100)
    except TypeError as e:
        print("No object in field of view")
        print(cont)
        
            


cam = cv2.VideoCapture(0)

while True:
    ret_val, img = cam.read()

    lower = np.array([135, 79, 39], dtype = "uint8")
    higher = np.array([255, 255, 255], dtype = "uint8")
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, w = img.shape[:2]
    flt = cv2.inRange(hsv, lower, higher);
    
    contours0, hierarchy = cv2.findContours(flt, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Only draw the biggest one
    #m.right(100)
    #bc = biggestContourI(contours0)
    bc=checkContour(contours0)
    
    cv2.drawContours(img,contours0, bc, (0,255,0), 3)
    cv2.imshow('my webcam', img)
    cv2.imshow('flt', flt)
    
    if cv2.waitKey(1) == 27:
        break  
cv2.destroyAllWindows()