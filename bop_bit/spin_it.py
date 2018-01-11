# Spin it
# https://trello.com/c/uUocRhe4

from microbit import *
import radio

radio.on()
radio.config(channel=69)

def is_triggered()
    zeroval = pin0.read_digital()
    pin0.set_pull(pin0.PULL_UP)
    oneval = pin1.read_digital()
    pin1.set_pull(pin0.PULL_UP)

    if zeroval == 1 or oneval == 1:
        return True
    else:
        return False