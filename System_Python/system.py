#!/usr/bin/env python
from motor import Motor
from encoder import Encoder

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
		self.encoder_linear = Encoder(encoder_clock_pin, encoder_linear_cs_pin, encoder_data_pin)
		self.encoder_linear.set_zero()
    # END __init__()
	
	# Get the values of the encoders to determine the angular and linear position of the pendulum.
	# Values are returned as a tuple: (angle, linear).
	### angle: 0 indicates the pendulum is exactly straight up.
	#####	   180 or -180 indicate the pendulum is exactly straight down.
	#####	   Positive values indicate the pendulum is leaning to the right.
	#####	   Negative values indicate the pendulum is leaning to the left.
	### linear: 0 indicates the pendulum is exactly in the middle of the track.
	#####		Positive values indicate the pendulum is right-of-center.
	#####		Negative values indicate the pendulum is left-of-center.
	def measure(self):
		angular_position = self.encoder_angular.read_position('Degrees')
		if angular_position > 180:
			angular_position = angular_position - 360
		# TODO: Implement linear position
		# Need to determine how to keep track of position based on gearing and rotations.
		#linear_position = self.encoder_linear.read_position('Raw')
		linear_position = 0
		return (angular_position, linear_position)
	# END measure()
	
	# Adjust the pendulum's linear position using the motor.
	### speed: Acceptable values range from -100 to 100 (as a percentage), with 100/-100 being the maximum adjustment speed.
	#####	   Negative values will move the pendulum to the left.
	#####	   Positive values will move the pendulum to the right.
	def adjust(self, speed):
		# cap the speed inputs
		if speed > 100.0:
			speed = 100.0
		if speed < -100.0:
			speed = -100.0
		# change the motor speed
		# TODO: Make sure the motor is oriented so that positive speed the correct direction (same for negative). Change the values otherwise.
		self.motor.move(speed)
	# END adjust()
# END System
    