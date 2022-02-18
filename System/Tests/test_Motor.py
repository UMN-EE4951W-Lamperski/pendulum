from pendulum import Motor
import time
import RPi.GPIO as GPIO

# Decide which pins to hook up to on the Pi before running
speed_pin = 17
forward_pin = 27
reverse_pin = 22

m = Motor(speed_pin, forward_pin, reverse_pin)

dir = 'ascending'
speed = 0.0
try:
    while 1:
        if speed >= 15.0:
            dir = 'descending'
        elif speed <= -15.0:
            dir = 'ascending'
        if dir == 'ascending':
            speed = speed + 2.0
        else:
            speed = speed - 2.0
        m.move(speed)
        time.sleep(0.1)
except:
    print("Program killed by Ctrl-C")
finally:
    GPIO.cleanup()