from microbit import *
import radio
import neopixel

unit_name = '' 
unit_colour = '' #will be set to the rounds colour for this unit
set_up = False

RAINBOW = [(128,0,0),(128,70,0),(128,128,0),(0,128,81),(0,64,0),(0,0,128),(75,0,128),(35,0,65),(128,65,170)]

npix = neopixel.NeoPixel(pin0, 30)
npix.clear()

colours = { 'red' : (128,0,0),
            'green' : (0,128,0),
            'blue' : (0,0,128),
            'yellow' : (128,128,0), 
            'white' : (128,128,128) }

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
    flash_delay = 500
    new_game = False
    wait_time = 0
    sad_wait_time = 0
    sad_delay = 1000
    sad_shift = False
    lit = False
    #while not message received. Make red flash
    while not new_game:
        current_time = running_time()
        #flashing lights
        if current_time > wait_time:
            if lit:
                npix.clear()
                lit = False
            else:
                lit = True
                light_all('red')
                
            wait_time = running_time() + flash_delay
            
        #sad face
        if current_time > sad_wait_time:
            if sad_shift:
                display.show(Image.SAD)
                sad_shift = False
            else:
                display.show(Image.SAD.shift_up(1))
                sad_shift = True
            sad_wait_time = running_time() + sad_delay
        
        msg = radio.receive()
        if msg:
            unit_call, instruction, value = msg_split(msg)
            if instruction == 'new_game':
                new_game = True
                display.clear()    

def round_finished():
    new_game = False
    n = 0
    wait_time = 0
    happy_wait_time = 0
    rainbow_delay = 100
    happy_delay = 1000
    happy_shift = False
    
    #until new_game message is received, flash rainbow and happy faces 
    while not new_game:
        current_time = running_time()
        #rainbows
        if current_time > wait_time:
            for pix in range(len(npix)):
                npix[(pix+n)%len(npix)] = RAINBOW[pix%len(RAINBOW)]
            npix.show()
            n += 1
            wait_time = running_time() + rainbow_delay
            
        #happy face
        if current_time > happy_wait_time:
            if happy_shift:
                display.show(Image.HAPPY)
                happy_shift = False
            else:
                display.show(Image.HAPPY.shift_up(1))
                happy_shift = True
            happy_wait_time = running_time() + happy_delay
        
        #getting message to see if new_game
        msg = radio.receive()
        if msg:
            unit_call, instruction, value = msg_split(msg)
            if instruction == 'new_game' or instruction == 'new_game':
                new_game = True
                display.clear()
                
def button_press(unit_colour):
    press_delay = 400
    radio.send(unit_name + ':pressed:1')   #check
    npix.clear()
    wait_time = running_time() + press_delay
    while running_time() < wait_time:
        continue
    light_all(unit_colour)

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
light_all('white')
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
        print(unit_call, instruction, value)
        
        if unit_call == unit_name or unit_call == 'all':
            if instruction == 'incorrect':
                incorrect()
            
            if instruction == 'round_finished':
                round_finished()
                
            if instruction == 'colour':
                set_colour(value)
                unit_colour = value     #sets global value to colour
            
    if pin1.read_digital():          #sends signal to centre
        button_press(unit_colour) 

#PROTOCOL    
#unit_call:instruction:value