from pendulum import System
import time
from sys import exit
#import pandas
from pendulum import Encoder

import RPi.GPIO as GPIO


clk_pin = 3
cs_pin  = 23
data_pin = 2

e = Encoder(clk_pin, cs_pin, data_pin)
e.set_zero()
###




sys = System(angular_units = 'Radians')

for x in range(4,20):
    linear = 0
    
    print("beginning of test with speed " + str(x))
    
    while linear > -7:
        sys.adjust(-5)
        angle, linear = sys.measure()
        print("Angle: " + str(angle) + ", Linear: " + str(linear))
        time.sleep(0.1)
    sys.adjust(0)
    time.sleep(3)    
    sys.add_log("this is a test with speed " + str(x))
    
    while linear < 7:
        sys.adjust(x)
        angle, linear = sys.measure()
        print("Angle: " + str(angle) + ", Linear: " + str(linear))
        sys.add_results(e.read_position('Degrees'), linear, x)
        time.sleep(0.1)
    sys.adjust(0)    
    print("end of test with speed " + str(x))
    time.sleep(3)
    

exit()








#class test():
#    def __init__(self, x, theta):
#        self.x = 0
#        self.theta = 0
#
#    def getINFO(self, theta):
#        #theta, x = self.System.measure()
#        theta, x = self.sys.measure()
#
#while(1):
#    test.getINFO()
#    print("t")
#    #print("theta",test.theta)
#    #print("x",test.x)
#
