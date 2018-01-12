from microbit import *
import radio
import neopixel
import random

npix = neopixel.NeoPixel(pin0, 7)

#colours
red = (128,0,0)
green = (0,128,0)
blue = (0,0,128)
yellow = (128,128,0)

def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()
    return

def Orientation(unit_name):
    while True: #tells player where each colour is at
    msg = radio.receive() #unit1:red EXAMPLE
    if msg:
        if msg.startswith(unit_name):
            colour = msg.split(':')[1]
            LightAll(colour)
            sleep(5000)
            npix.clear()
            break
            
#start up
radio.on()
radio.config(channel=73, group=2)
#to get name from center unit
radio.send("requestname")
unit_name = radio.receive()