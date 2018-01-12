from microbit import *
import radio
import random

radio.on()
radio.config(channel=71)

while True:
    msg = radio.receive()
    if msg:
        if msg == "SNSR_RNDM-1":
            display.show(random.randint(1,9))
        elif msg == '