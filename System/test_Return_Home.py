from pendulum import System
from time import sleep

sys = System()
sys.initialize()

ang,lin = sys.measure()

sys.torque(-100)

ang,lin = sys.measure()
sleep(0.01)
while lin > -20:
    ang,lin = sys.measure()
    sleep(0.01)

sys.return_home()
