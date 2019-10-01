import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PIN_CLK = 2
PIN_DATA = 3
PIN_CS  = 4
delay = 0.0000005

# pin setup done here
try:
    GPIO.setup(PIN_CLK,GPIO.OUT)
    GPIO.setup(PIN_DATA,GPIO.IN)
    GPIO.setup(PIN_CS,GPIO.OUT)                                                                                                    
    GPIO.output(PIN_CS,1)
    GPIO.output(PIN_CLK,1)
except:
    print("ERROR. Unable to setup the configuration requested")                                    

#wait some time to start
time.sleep(0.5)

print("GPIO configuration enabled")

def clockup():
    GPIO.output(PIN_CLK,1)
def clockdown():
    GPIO.output(PIN_CLK,0)

def readpos():
    GPIO.output(PIN_CS,0) #pulls low to start

    time.sleep(delay*2)
    data = 0
    clockdown()
    
    time1=time.clock()
    for i in range(0,10): #bitcount):
        clockup() #375 ns between each
        data<<=1  
        data|=GPIO.input(PIN_DATA)
        #while(time.clock()-time1<minReadValue);
        clockdown()
    print(time.clock()-time1)
    GPIO.output(PIN_CS,1) #pull high after finish
    
    return data

try:
    while(1):
        print(readpos())
        time.sleep(0.001)
        #break
        
finally:
    print("cleaning up GPIO")
    GPIO.cleanup()