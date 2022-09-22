from pymavlink import mavutil
import time
import serial
import arm_file
import time

from threading import Thread
import math

from pymavlink import mavutil

from pymavlink.quaternion import QuaternionBase

def arm():
    master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)
    # # wait until arming confirmed (can manually check with master.motors_armed())
    print("Waiting for the vehicle to arm")
    master.motors_armed_wait()
    print('Armed!')

def set_target_depth(depth):
    master.mav.set_position_target_global_int_send(
        int(1e3 * (time.time() - boot_time)), # ms since boot
        master.target_system, master.target_component,
        coordinate_frame=mavutil.mavlink.MAV_FRAME_GLOBAL_INT,
        type_mask=( # ignore everything except z position
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_X_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_Y_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_Z_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VZ_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_FORCE_SET |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE
        ), lat_int=0, lon_int=0, alt=depth, # (x, y WGS84 frame pos - not used), z [m]
        vx=0, vy=0, vz=0, # velocities in NED frame [m/s] (not used)
        afx=0, afy=0, afz=0, yaw=0, yaw_rate=0
    )

def set_target_attitude(roll, pitch, yaw):
    master.mav.set_attitude_target_send(
        int(1e3 * (time.time() - boot_time)), 
        master.target_system, master.target_component,
        mavutil.mavlink.ATTITUDE_TARGET_TYPEMASK_THROTTLE_IGNORE,
        QuaternionBase([math.radians(angle) for angle in (roll, pitch, yaw)]),
        0, 0, 0, 0 
    )


def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1900-1900
    """

    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(8)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.


master = mavutil.mavlink_connection("/dev/ttyACM0", baud=57600)
boot_time = time.time()
master.wait_heartbeat()
master.arducopter_arm()
master.motors_armed_wait()
arm()
DEPTH_HOLD = 'ALT_HOLD'
DEPTH_HOLD_MODE = master.mode_mapping()[DEPTH_HOLD]
while not master.wait_heartbeat().custom_mode == DEPTH_HOLD_MODE:
    master.set_mode(DEPTH_HOLD)
while (2<3):
	Thread(target = set_target_depth(-0.5)).start()
    

while True:
    Thread(target = set_rc_channel_pwm(4, 1550)).start()   



    