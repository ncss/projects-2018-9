from microbit import *
import radio
import neopixel
import random

npix = neopixel.NeoPixel(pin0, 7)

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()
    return

#start up
radio.on()
radio.config(channel=73, group="ncssgroup2")
#to get name from center unit
radio.send("requestname")
unit_name = radio.receive()

while True:
    msg = radio.receive() #unit1:red EXAMPLE
    if msg.startswith(unit_name):
        colour = msg.split(':')[1]
        LightAll(colour)
        sleep(5000)
        npix.clear()
        break
        
