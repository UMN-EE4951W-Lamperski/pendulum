from motor import Motor
import time

# Decide which pins to hook up to on the Pi before running
speed_pin = 15
forward_pin = 16
reverse_pin = 17

m = Motor(speed_pin, forward_pin, reverse_pin)

dir = 'ascending'
speed = 0.0
while 1:
	m.Move(speed)
	if speed >= 100.0:
		dir = 'descending'
	elif speed <= -100.0:
		dir = 'ascending'
	if dir == 'ascending':
		speed = speed + 0.5
	else:
		speed = speed - 0.5
	time.sleep(0.1)