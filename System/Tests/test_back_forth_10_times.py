from pendulum import System
from time import sleep
        
# Main program
#print("before system()call")
sys = System()
#print("after system() call")
sys.initialize()
#print("after sys.inintalize called")

#Go back and forth 10 times

ang,lin = sys.measure()
print("Starting position before moving: " + str(lin))
sys.adjust(15)
ang,lin = sys.measure()
sleep(0.01)
counter = 0
while (counter < 10):
    
    sys.adjust(15)
    ang,lin = sys.measure()
    sleep(0.01)
    while lin < 12:
        ang,lin = sys.measure()
        sleep(0.01)
        sys.add_results(ang,lin,15)

    sys.adjust(-15)
    ang,lin = sys.measure()
    sleep(0.01)
    while lin > -12:
        ang,lin = sys.measure()
        sleep(0.01)
        sys.add_results(ang,lin,-15)
   
    counter += 1

sys.return_home()
