from microbit import *

# assign colour names to each of the pins
red = pin0
green = pin1

#variable timer
time_ms = 10000

ON = 1023

while True:
    #decreasing time fraction
    for i in range(time_ms):
        print(int(time_ms/ON))
        print((int(time_ms/ON)*i))
        print(ON-((int(time_ms/ON)*i)))
        #green.write_analog(ON-((int(time_ms/ON)*i)))
   