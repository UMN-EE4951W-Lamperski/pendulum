from encoder import Encoder
import time

# Decide which pins to hook up to on the Pi before running
clk_pin = 2
cs_pin  = 4
data_pin = 3

e = Encoder(clk_pin, cs_pin, data_pin)
e.setZero()

while(1):
    print(e.readPosition('Degrees'))
    time.sleep(0.001)