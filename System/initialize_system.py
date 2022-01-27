# This file should be run on system startup. It will initialize the linear position to the center so that all tests originate from a proper position.
# The center is found by using the hardware limit switches
from system import System
import RPi.GPIO as GPIO
        
# Main program
print("Got to init")
sys = System()
sys.initialize()
GPIO.cleanup()


##debug version
#print("alive")
#sys = System()
#limit_negative_pin = 19
#while(1):
#    print(GPIO.input(limit_negative_pin))