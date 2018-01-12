from microbit import *
import radio
import neopixel
import random #currently not required, should only be used on central

flash_delay = 100
set_up = False
unit_name = '' 
lit = False

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

def set_colour(colour):
#Shows colour, until turned off
    light_all(colour)
    
def clear_colour():    
    npix.clear()
    
def incorrect():
    #while not message received. Make red flash
    while not new_game:
        current_time = running_time()
        display.show(Image.SAD)
        
        if current_time > wait_time:
            if lit:
                npix.clear()
                lit = False
            else:
                lit = True
                for pix in range(0, len(npix)):
                npix[pix] = colours[red]
                
            wait_time = running_time() + flash_delay

#start up
radio.on()
radio.config(channel=73, group=2)
#to get name from center unit
radio.send("requestname")
npix.clear()

while set_up == False:
    msg = radio.receive()
    if msg:
        if msg.startswith('setup'):
            unit_name = msg.split(':')[1]
            display.scroll(unit_name)
            print(unit_name)
            set_up = True    

while True:
    msg = radio.receive() #unit1:colour:red EXAMPLE
    if msg:
        msg = msg.split(':')
        
        if msg[0] == unit_name:
            if msg[1] == 'colour':
                set_colour(msg[2])
    
#unit_name:instruction:data

