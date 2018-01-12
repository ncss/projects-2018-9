from microbit import *
import radio
import neopixel

unit_name = '' 
unit_colour = '' #will be set to the rounds colour for this unit
set_up = False

RAINBOW = [(255,0,0),(255,140,0),(255,255,0),(0,255,162),(0,128,0),(0,0,255),(145,0,255),(75,0,130),(255,130,238),(0,0,0)]

npix = neopixel.NeoPixel(pin0, 10)
npix.clear()

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
    flash_delay = 300
    new_game = False
    wait_time = 0
    lit = False
    #while not message received. Make red flash
    while not new_game:
        current_time = running_time()
        display.show(Image.SAD)
        
        if current_time > wait_time:
            print(0)
            if lit:
                print(1)
                npix.clear()
                lit = False
            else:
                print(2)
                lit = True
                for pix in range(0, 10):
                    npix[pix] = colours['red']
                
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
    n = 0
    display.show(Image.HAPPY)
    while new_game != True:
        #rainbows
        for pix in range(len(npix)):
            npix[(pix+n)%len(npix)] = RAINBOW[pix%len(RAINBOW)]
        npix.show()
        n += 1
        
        msg = radio.receive()
        if msg:
            unit_call, instruction, value = msg_split(msg)
            if instruction == 'new_game':
                new_game = True
                display.clear()

def msg_split(msg):
    print(msg)
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
radio.config(channel=73)
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

