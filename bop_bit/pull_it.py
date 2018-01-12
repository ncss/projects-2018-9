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

client = Client(69, "pull_it")

debug = False

def is_triggered():
    value = pin0.read_analog()
    if debug:
        print(value)
    if value >= 1020:
        return True
    else:
        return False

while True:
    if is_triggered():
        client.send_trigger()
        if debug:
            print('yes')
    sleep(200)