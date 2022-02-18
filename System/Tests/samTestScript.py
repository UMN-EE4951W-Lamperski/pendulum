
import sys
sys.path.insert(0, '/home/pi/pendulum/System')
from System.system import System
import time
from sys import exit
#import pandas


sys = System(angular_units = 'Radians')

for x in range(0,10):
    angle, linear = sys.measure()
    print("Angle: " + str(angle) + ", Linear: " + str(linear))
    sys.add_results(linear, angle, angle)
    time.sleep(0.2)
    

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