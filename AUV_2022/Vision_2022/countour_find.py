import cv2
import numpy as np




image = cv2.imread('/home/crossfire/Programming projects/auv_testing/blue.jpg')
# img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ret, im = cv2.threshold(img_gray, 100, 120, cv2.THRESH_BINARY_INV)
# contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnt=contours[0]
# #print("\ncontours: ",contours)
# area=cv2.contourArea(cnt)
# img = cv2.drawContours(image, contours, -1, (0,255,75), 2)
# #print("\nContour area",area)
# x, y, w, h = cv2.boundingRect(cnt)
# cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

kernal = np.ones((5, 5), "uint8")
hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
blue_mask = cv2.dilate(blue_mask, kernal)
res_blue = cv2.bitwise_and(image, image,mask = blue_mask)
contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        imageFrame = cv2.rectangle(image, (x, y),(x + w, y + h),(255, 0, 0), 2)
        

# print("\n\n\n",x,y,w,h)
# show_image(im)
show_image(image)

