=!/usr/bin/python
import serial 
import time
from track import *
from libCompass import *
from rrb2 import
import math
def move_angle(angle):
    if angle < 0:
        angle = angle + 360 
    bearing = readDirection() move_angle = bearing - angle if move_angle > 180:
turn_right()
•lif move_angle < -180: turn_left()
elif (move_angle) < 180 and move_angle > 0:
turn_left()
*lit move_angle > -180 and move_angle < 0:
turn_right()
whil•(abs(angle - bearing)) > 5:
time.sleep(.2)
print abs(angle-bearing) bearing = readDirection()
stop()
print "angle", bearing
positionRobot(xpos, ypos, xpos_goal, ypos_goal):
print xpos, ypos, xpos_goal, ypos_goal
distance = math.sgrt((xpos_goal - ypos_robot)**2 + (ypos_goal - ypos_robot)\
**2)
angle = round(math.degrees(math.atan2((ypos_goal - ypos_robot), (xpos_goal \ - xpos_robot))))
print "angle",angle
move_angle(angle)
print distance
return distance, angle
xpos robot = int(raw input("Robot X Position: "))