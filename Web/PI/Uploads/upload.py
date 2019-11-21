import time, os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = " + current_time)

f = open("Results/results.txt", "w+")
f.write("THIS IS RESULTS TEXT\n")
f.write("Current Time = " + current_time)
f.close()
print("Running test.py for ~ 5 seconds.")
time.sleep(5) 
