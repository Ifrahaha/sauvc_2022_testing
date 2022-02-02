!/usr/bin/python
import time
from track import *
import math

xpos_robot = int(raw_input("Robot X Position: "))
ypos_robot = int(raw_input("Robot Y Position: ")) 
xpos_goal = int(raw_input("Goal X Position: ")) 
ypos_goal = int(raw input("Goal Y Position: "))

distance = math.sqrt((xpos_goal - ypos_robot)**2 + (ypos_goal - ypos_robot)**2)
angle = round(math.degrees(math.atan2((ypos_goal - ypos_robot), (xpos_goal - xpos_robot)))) 
if angle < 0:
    angle = angle + 360
print (angle)
#Turn to the right bearing
if (angle) < 180: 
    turn_right(angle)
else:
    turn_left(angle)
print (distance) 
forward(distance)