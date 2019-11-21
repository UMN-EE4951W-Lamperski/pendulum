import time, os, sys
from datetime import datetime

file_name =  os.path.basename(sys.argv[0])

file_name = file_name.split(".")[0]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = " + current_time)

f = open("Results/" + file_name + "_results", "w+")
f.write("THIS IS RESULTS TEXT\n")
f.write("Current Time = " + current_time)
f.close()
print("Running test.py for ~ 5 seconds.")
time.sleep(5) 
