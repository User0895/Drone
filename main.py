"""
# Before execution place controller on table and drone on floor
w/ blue LED facing controller.
"""

# Module imports.
import LocoDrone
import time

loco_drone = LocoDrone.LocoDrone()

# Connects and calibrates to drone and takes off.
loco_drone.connect()
loco_drone.drone_calibrate()
loco_drone.drone_takeoff()

# Determines what mode of operation the user would like then turns to that.
def invoke(input):
    if input.lower() == "tilt":
        loco_drone.set_mode(loco_drone.MODE_ACCELEROMETER)
    elif input.lower() == "control":
        loco_drone.set_mode(loco_drone.MODE_CONTROL)
    elif input.lower() == "joystick":
        loco_drone.set_mode(loco_drone.MODE_JOYSTICK)
    else:
        print("Invalid inpput.")
       
    
#DEFINITIONS--------------------------------------------------------------------------------

# Hover
def hover(wait=5):
    loco_drone.set_data(0, 0, 0)  
    time.sleep(wait) 

# Vertical (U/D) - Z value.
def vertical(value, wait=5):
    loco_drone.set_data(0, 0, value)  
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)

# Roll (L/R) - X value.
def roll_right(value=10, wait=5):
    loco_drone.set_data(value, 0, 0)
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)

# Pitch (B/F) - Y value.
def pitch_bf(value=25, wait=5):
    loco_drone.set_data(0, value, 0)
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)

# Roll/Pitch (L/R) - X, Y value.
def pitch_lr(value1=35, value2=40, wait=5):
    loco_drone.set_data(value1, value2, 0)
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)

# Flip drone.
def flip(input):
    if input.lower() == "left":
        loco_drone.left_flip_drone()
    elif input.lower() == "right":
        loco_drone.right_flip_drone()
    else:
        print("Invlaid input.")

    

#EXECUTION---------------------------------------------------------------------------------

vertical(1)
pitch_bf(25)
hover()

#END---------------------------------------------------------------------------------------

loco_drone.drone_land()
loco_drone.disconnect() 
