# Shout it
# https://trello.com/c/vV1Z4Y6Z

from microbit import *
import radio

radio.on()
radio.config(channel=69)

def is_triggered():
    prev_val = pin0.read_analog()
    sleep(200)
    pin_val = pin0.read_analog()
    print(prev_val, pin_val)
    if abs(pin_val-prev_val) >= 250:
        return True
    else:
        return False
    
while True:
    if is_triggered() == True:
        print('yes')
    else:
        print('no')