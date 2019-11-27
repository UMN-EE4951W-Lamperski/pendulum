# This test file implements a super simple control-type function for testing the System library.
# DO NOT TEST ON ASSEMBLED PHYSICAL SYSTEM! It will probably break it.
import time

from System.system import System
        
# Main program
sys = System(angular_units = 'Radians')
while 1:
    angle, linear = sys.measure()
    print("Angle: " + str(angle) + ", Linear: " + str(linear))
    time.sleep(0.2)
    
