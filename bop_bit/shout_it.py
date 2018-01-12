# Shout it
# https://trello.com/c/vV1Z4Y6Z

from microbit import *
import radio
import client

radio.on()
radio.config(channel=69)
client = Client(69, "shout_it")

debug = False

def is_triggered():
    prev_val = pin0.read_analog()
    sleep(200)
    pin_val = pin0.read_analog()
    if debug:
        print(prev_value, cur_value)
    if abs(pin_val-prev_val) >= 250:
        return True
    else:
        return False
    
while True:
    if is_triggered() == True:
        client.send_trigger()
        if debug:
            print('yes')