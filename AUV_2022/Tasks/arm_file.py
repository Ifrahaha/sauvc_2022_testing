from pymavlink import mavutil
import time
import serial

def arm():
    print("Initiating Connection")
    master = mavutil.mavlink_connection("/dev/ttyACM0")
    master.wait_heartbeat()
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0)

    print("Waiting for the vehicle to arm")
    master.motors_armed_wait()
    print('Armed!')