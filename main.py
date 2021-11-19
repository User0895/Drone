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

# Vertical,
def vertical(value, wait):
    loco_drone.set_data(0, value, 0)  
    time.sleep(wait)

# Hover
def hover(value, wait):
    loco_drone.set_data(0, value, 0)  
    time.sleep(wait) 
    
# Roll
def roll_right(value, wait):
    loco_drone.set_data(value, 0, 0)
    time.sleep(wait)

# Forward
def go_forward(value, wait):
    loco_drone.set_data(0, value, 0)
    time.sleep(wait)
    loco_drone.set_data(0, 0, 0)
    
#EXECUTION---------------------------------------------------------------------------------

vertical(2, 1)
hover(0, 1)
go_forward(2, 1)
hover(0, 1)
vertical(-2, 1)

#END---------------------------------------------------------------------------------------

loco_drone.drone_land()
loco_drone.disconnect() 
