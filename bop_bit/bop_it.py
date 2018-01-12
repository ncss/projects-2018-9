# Bop it
# https://trello.com/c/vSm7z3AP

from microbit import *
#connect to pin 0 and 3V

def is_triggered():
    pressed = pin0.read_digital()
    if pressed == 0:
        print('yes')
        return True
    else:
        print('no')
        return False


