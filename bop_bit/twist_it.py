# Twist it
# https://trello.com/c/4iY78h2T

from microbit import *
import radio
debug = False

class Client:
    """Sends trigger messages to a server on the same channel"""
    def __init__(self, chan, name):
        self.channel = chan
        self.name = name.lower()
        radio.on()
        radio.config(channel = self.channel)
        #print("Configured Client")

    def send_trigger(self):
        message = self.name
        message += ":"
        message += "triggered"
        radio.send(message)
        #print("Sent: " + message)

    def send_alive(self):
        message = self.name
        message += ":"
        message += "alive"
        #print("Sent: " + message)

def is_triggered():

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
    
        # anti-clockwise
        if pin_state_a and pin_state_a != pin_last_a: # check is on and rising edge
            if (not pin_state_b and pin_state_a):     # check if before other pin
                counter -= 1
    
        if debug:
            print(str(counter), wait=False)
        # remember states
        pin_last_a = pin_state_a
        pin_last_b = pin_state_b
        
        #check twisted enough
        if abs((counter))>5:
            display.show(Image.HAPPY)
            return True
        else:
            display.show(Image.SAD)