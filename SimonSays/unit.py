from microbit import *
import radio
import neopixel
import random #currently not required, should only be used on central

npix = neopixel.NeoPixel(pin0, 7)

colours = { 'red' : (255,0,0),
            'green' : (0,255,0),
            'blue' : (0,0,255),
            'yellow' : (255,255,0) }


def light_all(colour):
    for pix in range(0, len(npix)):
        npix[pix] = colours[colour]
    npix.show()
    return

set_up = False
unit_name = ''

def Orientation(unit_name):
    while True: #tells player where each colour is at
    msg = radio.receive() #unit1:red EXAMPLE
    if msg:
        if msg.startswith(unit_name):
            colour = msg.split(':')[1]
            light_all(colour)
            sleep(5000)
            npix.clear()
            break
            
#start up
radio.on()
radio.config(channel=73, group=2)
#to get name from center unit
radio.send("requestname")

while set_up == False:
    msg = radio.receive()
    if msg:
        if msg.startswith('setup'):
            unit_name = msg.split(':')[1]
            display.scroll(unit_name)
            print(unit_name)
            set_up = True    

while True:
    msg = radio.receive() #unit1:red EXAMPLE
    if msg:
        print(msg)
        if msg.startswith(unit_name):
            print('in thing')
            colour = msg.split(':')[1]
            light_all(colour)
            sleep(5000)
            npix.clear()
            break
    


