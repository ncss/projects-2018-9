# Spin it
# https://trello.com/c/uUocRhe4

from microbit import *
import radio
import client

client = Client(69, "spin_it")

debug = False

cur_value = 0;
prev_value = 0;

def is_triggered():
    prev_value = pin1.read_analog()
    if debug print(prev_value, cur_value)
    if abs(cur_value-prev_value) >= 100:
        cur_value = prev_value
        return True
    else:
        return False

while True:
    if is_triggered():
        client.send_trigger()
        if debug print('yes')
