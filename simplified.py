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
       
wait = 10
    
#DEFINITIONS--------------------------------------------------------------------------------

# Hover - ISSUE: Drone heavily skewed to the left. Issue with syncing or code?
loco_drone.set_data(0, 0, 0)  
time.sleep(wait) 

# Roll (Left)
loco_drone.set_data(10, 0, 0)
time.sleep(wait)
loco_drone.set_data(0, 0, 0)

# Roll (Right).
loco_drone.set_data(-20, 0, 0)
time.sleep(wait)
loco_drone.set_data(0, 0, 0)

# Pitch (Forward)
loco_drone.set_data(0, 25, 0)
time.sleep(wait)
loco_drone.set_data(0, 0, 0)

# Pitch (Backward)
loco_drone.set_data(0, -30, 0)
time.sleep(wait)
loco_drone.set_data(0, 0, 0)

# Roll/Pitch (L/R) - X, Y value. - SEE previous.
def roll_pitch(input):
    if input.lower() == "lf" or "l/f":
        loco_drone.set_data(45, 30, 0)
    elif input.lower() == "rf" or "r/f":
        loco_drone.set_data(-45, 30, 0)
    elif input.lower() == "lb" or "l/b":
        loco_drone.set_data(-45, -30, 0)
    else:
        loco_drone.set_data(45, -30, 0)
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)

# Flip drone. WORKS
def flip(input):
    if input.lower() == "left":
        loco_drone.left_flip_drone()
    elif input.lower() == "right":
        loco_drone.right_flip_drone()
    else:
        print("Invalid input.")

#EXECUTION---------------------------------------------------------------------------------

vertical()
pitch_bf()
hover()

#END---------------------------------------------------------------------------------------

loco_drone.drone_land()
loco_drone.disconnect() 
