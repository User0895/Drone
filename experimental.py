"""
# Before execution place controller on table and drone on floor
w/ blue LED facing controller.
"""

# Module imports.
import LocoDrone
import time

loco_drone = LocoDrone.LocoDrone()

# Determines what mode of operation the user would like then turns to that.
def invoke(input):
    if input.lower() == "tilt":
        loco_drone.set_mode(loco_drone.MODE_ACCELEROMETER)
    elif input.lower() == "control" or "default":
        loco_drone.set_mode(loco_drone.MODE_CONTROL)
    elif input.lower() == "joystick":
        loco_drone.set_mode(loco_drone.MODE_JOYSTICK)
    else:
        print("Invalid input.")

# Connects and calibrates to drone and takes off.
loco_drone.connect()
loco_drone.controller_calibrate()
loco_drone.drone_calibrate()
loco_drone.drone_takeoff()
invoke("default")
    
#DEFINITIONS--------------------------------------------------------------------------------

def move(x,y,z,wait=10):
    loco_drone.set_data(x, y, z)
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)

def flip(input):
    if input.lower() == "left":
        loco_drone.left_flip_drone()
    elif input.lower() == "right":
        loco_drone.right_flip_drone()
    else:
        print("Invalid input.")    

#EXECUTION---------------------------------------------------------------------------------

move(1,2,3)

#END---------------------------------------------------------------------------------------

loco_drone.drone_land()
loco_drone.disconnect() 
