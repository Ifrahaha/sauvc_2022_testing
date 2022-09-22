from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection("/dev/ttyACM0", baud=57600)
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# https://mavlink.io/en/messages/common.html#MAV_CMD_COMPONENT_ARM_DISARM

# Arm
# master.arducopter_arm() or:
# master.mav.command_long_send(
#     master.target_system,
#     master.target_component,
#     mavutil.mavlink.MAV_CMD_DO_S,
#     0, 0, 5, 0, 0, 0, 0, 0)

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED,
    0, 0, 100, 0, 0, 0, 0, 0)
