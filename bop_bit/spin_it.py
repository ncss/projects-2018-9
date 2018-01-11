# Spin it
# https://trello.com/c/uUocRhe4

from microbit import *
import radio

radio.on()
radio.config(channel=69)

def is_triggered():
    prev_value = pin1.read_analog()
    sleep(500)
    cur_value = pin1.read_analog()
    print(prev_value, cur_value)
    if abs(cur_value-prev_value) >= 100:
        return True
    else:
        return False

while True:
    if is_triggered():
        print('yes')
    else:
        print('no')


