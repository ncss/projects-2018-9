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

client = Client(69, "twist_it")

pin_last_a = False
counter = 0
counter_last = 0

# set pullups
pin0.read_digital()
pin0.set_pull(pin0.PULL_UP)

while True:
    # get states
    pin_state_a = pin0.read_digital()
    
    # clockwise
    if pin_state_a and not pin_last_a: # check is on and rising edge
        counter += 1
        if debug: print(str(counter))
    pin_last_a = pin_state_a
    

    # check for twisting
    if counter != counter_last:
        display.show(Image.HAPPY)
        client.send_trigger()
        sleep(500)
    else:
        display.show(Image.SAD)
    counter_last = counter