# Bop it
# https://trello.com/c/vSm7z3AP

from microbit import *
#connect to pin 0 and 3V

debug = False

def is_triggered():
    pressed = pin0.read_digital()
    if pressed == 0:
        if debug:
            print('yes')
        return True
    else:
        if debug:
            print('no')
        return False


