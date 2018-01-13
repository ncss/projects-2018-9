from microbit import *
import radio
display.show(Image.ALL_CLOCKS, loop=True, delay=500, wait=False)

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
    prev_val = pin0.read_analog()
    sleep(50)
    cur_val = pin0.read_analog()
    difference = prev_val-cur_val

    if debug:
        print(difference)
    if prev_val != cur_val and abs(difference)!= 1 :
        return True
    else:
        return False

while True:
    if is_triggered():
        client.send_trigger()
        display.show(Image.HAPPY, delay=400, wait=False, clear=True)
        if debug:
            print('yes')
    sleep(200)
