# Shout it
# https://trello.com/c/vV1Z4Y6Z

from microbit import *
import radio

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

client = Client(69, "spin_it")

debug = False 

cur_val = 0
prev_val = 0
    
while True:
    cur_val = pin0.read_analog()
    if debug: print(prev_val, cur_val)
    if abs(cur_val-prev_val) >= 500:
        client.send_trigger()
        if debug:
            print('yes')
    prev_val = cur_val
  