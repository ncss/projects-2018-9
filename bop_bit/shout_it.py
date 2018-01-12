# Shout it
# https://trello.com/c/vV1Z4Y6Z

from microbit import *
import radio
import client

client = Client(69, "spin_it")

debug = False

def is_triggered():
    prev_val = pin0.read_analog()
    sleep(100)
    pin_val = pin0.read_analog()
    if debug:
        print(prev_val, pin_val)
    if abs(pin_val-prev_val) >= 550:
        return True
    else:
        return False
    
while True:
    if is_triggered() == True:
        client.send_trigger()
        if debug:
            print('yes')