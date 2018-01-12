# Twist it
# https://trello.com/c/4iY78h2T

from microbit import *

# Read output from quadrature encoder module
# and print to screen

pin_last_a = False
pin_last_b = False
counter = 0

# set pullups
pin0.read_digital()
pin0.set_pull(pin0.PULL_UP)
pin13.read_digital()
pin13.set_pull(pin13.PULL_UP)

while True:
    # get states
    pin_state_a = pin0.read_digital()
    pin_state_b = pin13.read_digital()
    
    # clockwise
    if pin_state_b and pin_state_b != pin_last_b: # check is on and rising edge
        if (not pin_state_a and pin_state_b):     # check if before other pin
            counter += 1
            #print("up") # debug
    
    # anti-clockwise
    if pin_state_a and pin_state_a != pin_last_a: # check is on and rising edge
        if (not pin_state_b and pin_state_a):     # check if before other pin
            counter -= 1
            #print("down") # debug
    
    display.scroll(str(counter), wait=False);     # display
    
    # remember states
    pin_last_a = pin_state_a
    pin_last_b = pin_state_b