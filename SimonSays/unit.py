from microbit import *
import radio
import neopixel

unit_name = '' 
unit_colour = '' #will be set to the rounds colour for this unit
lit = False
set_up = False

npix = neopixel.NeoPixel(pin0, 10)

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
    new_game = False
    display.show(Image.HAPPY)
    while new_game != True:
        #scroll rainbows
        display.show(Image.HAPPY)
        
        msg = radio.receive()
        if msg:
            unit_call, instruction, value = msg_split(msg)
            if instruction == 'new_game':
                new_game = True

def msg_split(msg):
    msg = msg.split(':')
    if len(msg) != 3:
        return('','','')
        #break
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
display.clear()

while set_up == False:
    display.show(Image.SQUARE)
    msg = radio.receive()
    if msg:
        unit_call, instruction, value = msg_split(msg)
        #print(unit_call, instruction, value)
        if instruction == 'setup':
            unit_name = unit_call
            #display.scroll(unit_name)   #testing
            print(unit_name)            #testing
            display.clear()
            set_up = True  

#main loop
while True:
    msg = radio.receive() #EXAMPLE: unit1:colour:red
    if msg:
        unit_call, instruction, value = msg_split(msg)
        #print(unit_call, instruction, value)
        
        if unit_call == unit_name:
            if instruction == 'incorrect':
                incorrect()
            
            if instruction == 'round_finished':
                round_finished()
                
            #if instruction == 'new_round':    
            
            if instruction == 'colour':
                set_colour(value)
                unit_colour = value     #sets global value to colour
            
    if button_a.was_pressed():          #sends signal to centre
        button_press(unit_colour) 

#PROTOCOL    
#unit_call:instruction:value

