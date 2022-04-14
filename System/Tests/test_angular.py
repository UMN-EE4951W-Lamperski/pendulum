from pendulum import System
from time import sleep
        
# Main program
#print("before system()call")
sys = System()
#print("after system() call")
sys.initialize()
#print("after sys.inintalize called")

ang,lin = sys.measure()
print("Starting position before moving: " + str(lin))
sys.adjust(0)
ang,lin = sys.measure()
sleep(1.0)
while lin < 10:
    ang,lin = sys.measure()
    sleep(0.01)
sys.return_home()
