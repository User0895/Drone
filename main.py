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

#DEFINITIONS--------------------------------------------------------------------------------

# Hover
def hover(value, wait):
    # Should X be zero?
    loco_drone.set_data(0, value, 0)  
    time.sleep(wait) 

# Vertical - Z value.
def vertical(value, wait):
    loco_drone.set_data(0, 0, value)  
    time.sleep(wait)

# Roll - X value.
def roll_right(value, wait):
    loco_drone.set_data(value, 0, 0)
    time.sleep(wait)

# Pitch (B/F) - Y value.
def pitch_1(value, wait):
    loco_drone.set_data(0, value, 0)
    time.sleep(wait)

# Roll/Pitch (L/R) - X, Y value.
def pitch_2(value1, value2, wait):
    loco_drone.set_data(value1, value2, 0)
    time.sleep(wait)

# Flip drone.
def flip(input):
    while True:
        if input.lower() == "left":
            loco_drone.left_flip_drone()
            break
        elif input.lower() == "right":
            loco_drone.right_flip_drone()
            break
        else:
            print("Invlaid input.")
            continue
    
# Forward
def go_forward(value, wait):
    loco_drone.set_data(0, value, 0)
    time.sleep(wait)
    
#JOYSTICK----------------------------------------------------------------------------------

#Start Joystick Controls
"""
loco_drone.set_mode(loco_drone.MODE_JOYSTICK)
time.sleep(300)
loco_drone.set_mode(loco_drone.MODE_CONTROL)
"""


#EXECUTION---------------------------------------------------------------------------------

vertical(2, 1)
hover(0, 1)
go_forward(3, 1)
vertical(-2, 1)

#END---------------------------------------------------------------------------------------

loco_drone.drone_land()
loco_drone.disconnect() 
