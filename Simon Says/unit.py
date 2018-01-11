from microbit import *
import radio
import neopixel
import random

unit_name = "unit1"

#start up
radio.on()
radio.config(channel=73, group="ncssgroup2")
#to get name from center unit
radio.send("requestname")
unit_name = radio.receive()

while True:
    colour = radio.receive()
    if colour:
        
