#!/usr/bin/env python
from motor import Motor
from encoder import Encoder
import math

# IO pin definitions
### Motor pins
motor_speed_pin = 17
motor_forward_pin = 27
motor_reverse_pin = 22
### Encoder pins (shared by both encoders)
encoder_clock_pin = 2
encoder_data_pin = 3
### Angular encoder pins
encoder_angular_cs_pin = 4
### Linear encoder pins
encoder_linear_cs_pin = 5


# System Class
# This is the primary interface a student will use to control the pendulum.
class System:
    def __init__(self):
        # Initialize the motor.
        self.motor = Motor(motor_speed_pin, motor_forward_pin, motor_reverse_pin)
        # Initialize the angular encoder.
        self.encoder_angular = Encoder(encoder_clock_pin, encoder_angular_cs_pin, encoder_data_pin)
        self.encoder_angular.set_zero()
        # Initialize the linear encoder.
        self.encoder_linear = Linear_Encoder(encoder_clock_pin, encoder_linear_cs_pin, encoder_data_pin)
        self.encoder_linear.set_zero()
    # END __init__()
    
    # Get the values of the encoders to determine the angular and linear position of the pendulum.
    # Values are returned as a tuple: (angle, linear).
    ### angle: 0 indicates the pendulum is exactly straight up.
    #####      180 or -180 indicate the pendulum is exactly straight down.
    #####      Positive values indicate the pendulum is leaning to the right.
    #####      Negative values indicate the pendulum is leaning to the left.
    ### linear: 0 indicates the pendulum is exactly in the middle of the track.
    #####       Positive values indicate the pendulum is right-of-center.
    #####       Negative values indicate the pendulum is left-of-center.
    def measure(self):
        angular_position = self.encoder_angular.read_position('Degrees')
        if angular_position > 180:
            angular_position = angular_position - 360
        #linear_position = self.encoder_linear.read_position()
        linear_position = 0
        return (angular_position, linear_position)
    # END measure()
    
    # Adjust the pendulum's linear position using the motor.
    ### speed: Acceptable values range from -100 to 100 (as a percentage), with 100/-100 being the maximum adjustment speed.
    #####      Negative values will move the pendulum to the left.
    #####      Positive values will move the pendulum to the right.
    def adjust(self, speed):
        # cap the speed inputs
        if speed > 100.0:
            speed = 100.0
        if speed < -100.0:
            speed = -100.0
        # change the motor speed
        # TODO: Make sure the motor is oriented so that positive speed the correct direction (same for negative). Change the values otherwise.
        self.motor.coast()
        self.motor.move(speed)
    # END adjust()
# END System

# Linear Encoder class
# This class is to help with using an absolute encoder for linear position sensing as assembled in the physical system.
# The function definitions here are the same as with the regular encoder (pseudo-interface).
class Linear_Encoder:
    DIAMETER = 4.0 # MEASURE THIS
    
    def __init__(self, clk_pin, cs_pin, data_pin):
        self.encoder = Encoder(clk_pin, cs_pin, data_pin)
        self.set_zero()
    def set_zero(self):
        # Set the zero position for the encoder
        self.encoder.set_zero()
        # Reset the internal position counter
        self.rotations = 0
        self.last_position = 0
    def read_position(self):
        # Read the position of the encoder 
        position = self.encoder.read_position('Raw')
        # Compare to last known position
        # NOTE: For now, assume that we are moving the smallest possible distance (i.e. 5 -> 1 is -4, not 1020)
        if position - self.last_position > 0:
            if position < 512 and self.last_position > 512:
                # We are moving to the right (positive) and have completed a new rotation
                self.rotations = self.rotations + 1
        else:
            if position > 512 and self.last_position < 512:
                # We are moving to the left (negative) and have completed a new rotation
                self.rotations = self.rotations - 1
        # Save the last position for the next calculation
        self.last_position = position
            
        # compute the position based on the system parameters
        # linear position = (2pi*r)(n) + (2pi*r)(position/1024) = (2pi*r)(n + position/1024) = (pi*d)(n + position/1024)
        return (math.pi*DIAMETER)*(self.rotations + position/1024)
