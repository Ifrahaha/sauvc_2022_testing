import cv2
import numpy as np
import math
import serial
import movement

# import picamera
# import picamera.array
m = movement.Movement()

threshold1 = 85
threshold2 = 85
theta=0
r_width = 500
r_height = 300
minLineLength = 5
maxLineGap = 10
k_width = 5
k_height = 5
max_slider = 10

# Linux System Serial Port
# ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)           # linux

# Read Image
image = cv2.imread(r'C:\Users\aasai\Desktop\new1.jpeg')
# Resize width=500 height=300 incase of inputting raspi captured image
image = cv2.resize(image,(r_width,r_height))
# Convert the image to gray-scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# given input image, kernel width =5 height = 5, Gaussian kernel standard deviation
blurred = cv2.GaussianBlur(gray, (k_width, k_height), 0)
# Find the edges in the image using canny detector
edged = cv2.Canny(blurred, threshold1, threshold2)
# Detect points that form a line
lines = cv2.HoughLinesP(edged,1,np.pi/180,max_slider,minLineLength,maxLineGap)
print(lines[0])
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(image,(x1,y1),(x2,y2),(255,0,0),3)
        theta=theta+math.atan2((y2-y1),(x2-x1))
        print(theta)
threshold=5
if(theta>threshold):
    m.left(100)
    print("Go left")
if(theta<-threshold):
    m.right(100)
    print("Go right")
if(abs(theta)<threshold):
    m.forward(100)
    print("Go straight")
theta=0
cv2.imshow("Gray Image",gray)
cv2.imshow("blurred",blurred)
cv2.imshow("Edged",edged)
cv2.imshow("Line Detection",image)
cv2.waitKey(0)
cv2.destroyAllWindows()