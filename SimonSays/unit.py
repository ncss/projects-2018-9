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
        msg = msg.split(':')
        unit_call = msg[0]
        instruction = msg[1]
        value = msg[2]
        
        if instruction == 'setup':
            unit_name == unit_call
            display.scroll(unit_name)   #testing
            print(unit_name)            #testing
            set_up = True    

while True:
    msg = radio.receive() #EXAMPLE: unit1:colour:red
    if msg:
        msg = msg.split(':')
        unit_call = msg[0]
        instruction = msg[1]
        value = msg[2]
        
        if unit_call == unit_name:
            if instruction == 'incorrect':
                incorrect()
            
            if instruction == 'colour':
                set_colour(value)
                
    if button_a.was_pressed():      #sends signal to centre
        radio.send(unit_name + ':pressed:1')
    
#unit_call:instruction:value

