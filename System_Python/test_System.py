# This test file implements a super simple control-type function for testing the System library.
# DO NOT TEST ON ASSEMBLED PHYSICAL SYSTEM! It will probably break it.
import time

from system import System

# Return a speed based on current encoder angle.
# Convert an angle to speed (180 degrees = max speed)
def control_function(angle):
    return (abs(angle) / 180.0) * 100.0
        
# Main program
sys = System()
while 1:
    angle, linear = sys.measure()
    #print(angle)
    speed = control_function(angle)
    print(speed)
    sys.adjust(speed)
    time.sleep(0.05)
    