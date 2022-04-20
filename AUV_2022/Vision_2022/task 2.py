
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

greenLower = (38, 102, 84)
greenUpper = (74, 244, 147)

blueLower = (38, 102, 84)
blueUpper = (74, 244, 147)
pts = deque(maxlen=64)
bpts = deque(maxlen=64)


vs1 = VideoStream(src=0).start()
vs2 = VideoStream(src=1).start()


time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	frame = vs1.read()

	
	if frame is None:
		break

	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)


	(h, w) = frame.shape[:2] #w:image-width and h:image-height
	cv2.circle(frame, (w//2, h//2), 3, (255, 255, 255), -1) 
	#cv2.circle(frame, (w//2, h//2), 113, (255, 255, 255), -1) 
	color = (255, 0, 0)
	thickness = 1
	(h, w) = frame.shape[:2] #h=y-axis, w=x-axis
	
	# start_point =(0,0)
	# end_point =((w/3),(h/3))
	# cv2.rectangle(frame, start_point, end_point, color, thickness)


	# start_point =((w/3),0)
	# end_point =((2*w/3),(h/3))
	# cv2.rectangle(frame, start_point, end_point, color, thickness)

	# start_point =((2*w/3),0)
	# end_point =((2*w/3),(h/3))
	# cv2.rectangle(frame, start_point, end_point, color, thickness)


	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

    	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)



	# update the points queue
	pts.appendleft(center)

    	# loop over the set of tracked points
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
		
		(h, w) = frame.shape[:2] #h=y-axis, w=x-axis
		cx=w/2
		cy=h/2

		#detecting green

		if (pts[i][0]<(w/3) and pts[i][1]<(h/3)):
			print("up left")

		if (pts[i][0]>(w/3) and pts[i][0]<(2*w/3) and pts[i][1]<(h/3)):
			print("up")

		if (pts[i][0]>(2*w/3) and pts[i][1]<(h/3)):
			print("up right")

		if (pts[i][0]<(w/3) and pts[i][1]>(h/3) and pts[i][1]<(2*h/3)):
			print("left")

		if (pts[i][0]>(w/3) and pts[i][0]<(2*w/3) and pts[i][1]>(h/3) and pts[i][1]<(2*h/3)):
			print("center")

		if (pts[i][0]>(2*w/3) and pts[i][1]>(h/3) and pts[i][1]<(2*h/3)):
			print("right")

		if (pts[i][0]<(w/3) and pts[i][1]>(2*h/3)):
			print("down left")

		if (pts[i][0]>(w/3) and pts[i][0]<(2*w/3) and pts[i][1]>(2*h/3)):
			print("down")

		if (pts[i][0]>(2*w/3) and pts[i][1]>(2*h/3)):
			print("down right")

	while(len(pts)==0)
		frame1 = vs2.read()
		if frame1 is None:
			break
		frame1 = imutils.resize(frame1, width=600)
		blurred = cv2.GaussianBlur(frame1, (11, 11), 0)
		hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv, blueLower, blueUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		center = None
		if len(cnts) > 0:
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			if radius > 10:
				cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)

		bpts.appendleft(center)
		for i in range(1, len(bpts)):
		# if either of the tracked points are None, ignore
		# them
			if bpts[i - 1] is None or bpts[i] is None:
				continue

			# otherwise, compute the thickness of the line and
			# draw the connecting lines
			thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
			cv2.line(frame1, bpts[i - 1], bpts[i], (0, 0, 255), thickness)
			
			(h, w) = frame1.shape[:2] #h=y-axis, w=x-axis
			cx=w/2
			cy=h/2

			#detecting green
			counter=0
			if (bpts[i][0]<(w/3) and bpts[i][1]<(h/3)):
				#print("up left")
				print("forward")

			if (bpts[i][0]>(w/3) and bpts[i][0]<(2*w/3) and bpts[i][1]<(h/3)):
				#print("up")
				print("forward")

			if (bpts[i][0]>(2*w/3) and bpts[i][1]<(h/3)):
				#print("up right")
				print("forward")

			if (bpts[i][0]<(w/3) and bpts[i][1]>(h/3) and bpts[i][1]<(2*h/3)):
				count = count + 1
				print("left")

			if (bpts[i][0]>(w/3) and bpts[i][0]<(2*w/3) and bpts[i][1]>(h/3) and bpts[i][1]<(2*h/3)):
				count = count + 1
				print("center")

			if (bpts[i][0]>(2*w/3) and bpts[i][1]>(h/3) and bpts[i][1]<(2*h/3)):
				count = count + 1
				print("right")

			if (bpts[i][0]<(w/3) and bpts[i][1]>(2*h/3)):
				#print("down left")
				print("backward")

			if (bpts[i][0]>(w/3) and bpts[i][0]<(2*w/3) and bpts[i][1]>(2*h/3)):
				#print("down")
				print("backward")

			if (bpts[i][0]>(2*w/3) and bpts[i][1]>(2*h/3)):
				#print("down right")
				print("backward")


		

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	#print(pts)
	
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
	vs.stop()

# otherwise, release the camera
else:
	vs.release()

# close all windows
cv2.destroyAllWindows()