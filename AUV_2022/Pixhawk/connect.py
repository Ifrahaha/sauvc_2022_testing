from pymavlink import mavutil

# Create the connection
# Need to provide the serial port and baudrate
master = mavutil.mavlink_connection("/dev/ttyACM0")

# Restart the ArduSub board !
print('Connected')
master.reboot_autopilot()
