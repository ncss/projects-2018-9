from microbit import *
import radio
import neopixel
import random #currently not required, should only be used on central

set_up = False
unit_name = '' 
lit = False
unit_colour = '' #will be set to the rounds colour for this unit

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
    flash_delay = 100
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
            
def button_press(unit_colour):
    press_delay = 400
    radio.send(unit_name + ':pressed:1')   #check
    npix.clear()
    wait_time = running_time() + press_delay
    while running_time() < wait_time:
        continue
    light_all(unit_colour)

def round_finished():
    display.show(Image.HAPPY)
    #scroll rainbows
    while != new_game:
        #scroll rainbowa
        display.show(Image.HAPPY)
        
        msg = radio.receive()
        if msg:
            unit_call, instruction, value = msg_split(msg)

def msg_split(msg):
    msg.split(':')
    unit_call = msg[0]
    instruction = msg[1]
    value = msg[2]
    return(unit_call, instruction, value)
        

#START
radio.on()
radio.config(channel=73, group=2)
#to get name from center unit
radio.send("requestname")
npix.clear()

while set_up == False:
    msg = radio.receive()
    if msg:
        unit_call, instruction, value = msg_split(msg)
        
        if instruction == 'setup':
            unit_name == unit_call
            display.scroll(unit_name)   #testing
            print(unit_name)            #testing
            set_up = True    

while True:
    msg = radio.receive() #EXAMPLE: unit1:colour:red
    if msg:
        unit_call, instruction, value = msg_split(msg)
        
        if unit_call == unit_name:
            if instruction == 'incorrect':
                incorrect()
            
            if instruction == 'colour':
                set_colour(value)
                unit_colour = value     #sets global value to latest colour
            
    if button_a.was_pressed():          #sends signal to centre
        button_press(unit_colour)   
    
#unit_call:instruction:value

