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
loco_drone.set_mode(loco_drone.MODE_CONTROL)
       
wait = 5
    
#DEFINITIONS--------------------------------------------------------------------------------

# Hover - FUNCTIONAL: Still skewed.
loco_drone.set_data(0, 0, 0)  
time.sleep(10) 

invoke("joystick")
time.sleep(50)

# Roll (Left) - FUNCTIONAL: Tilt is minor.
#loco_drone.set_data(10, 0, 0)
#time.sleep(5)
#loco_drone.set_data(0, 0, 0)

# Roll (Right) - FUNCTIONAL: Tilt is minor.
#loco_drone.set_data(-20, 0, 0)
#time.sleep(wait)
#loco_drone.set_data(0, 0, 0)

# Pitch (Forward) - FUNCTIONAL
#loco_drone.set_data(0, 25, 0)
#time.sleep(5)
#loco_drone.set_data(0, 0, 0)

# Pitch (Backward) - FUNCTIONAL
#loco_drone.set_data(0, -30, 0)
#time.sleep(wait)
#loco_drone.set_data(0, 0, 0)

# Roll/Pitch (L/R) - X, Y value. - SEE previous.
def roll_pitch(input):
    if input.lower() == "lf" or "l/f": # FUNCTIONAL?.
        loco_drone.set_data(45, 30, 0)
    elif input.lower() == "rf" or "r/f": # 
        loco_drone.set_data(-45, 30, 0)
    elif input.lower() == "lb" or "l/b":
        loco_drone.set_data(-45, -30, 0)
    elif input.lower() == "rb" or "r/b":
        loco_drone.set_data(45, -30, 0)
    else:
        print("Invalid input.")
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)

#roll_pitch("lf")

# Roll/Pitch LF - FUNCTIONAL
#loco_drone.set_data(45, 30, 0)
#time.sleep(wait)
#loco_drone.set_data(0, 0, 0)

# Roll/Pitch RF - FUNCTIONAL
#loco_drone.set_data(-45, 30, 0)
#time.sleep(wait)
#loco_drone.set_data(0, 0, 0)

# Roll/Pitch LB - FUNCTIONAL
#loco_drone.set_data(-45, -30, 0)
#time.sleep(wait)
#loco_drone.set_data(0, 0, 0)

# Roll/Pitch RB - FUNCTIONAL
#loco_drone.set_data(45, -30, 0)
#time.sleep(3)
#loco_drone.set_data(0, 0, 0)

# Flip Drone - FUNCTIONAL.
def flip(input):
    if input.lower() == "left":
        loco_drone.left_flip_drone()
    elif input.lower() == "right":
        loco_drone.right_flip_drone()
    else:
        print("Invalid input.")

for i in range(10):
    flip("left")
    hover()
    flip("right")

#END---------------------------------------------------------------------------------------

loco_drone.drone_land()
loco_drone.disconnect() 
