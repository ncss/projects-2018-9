from microbit import *
import radio
import random
import music
# RNDM

radio.on()
radio.config(channel=71)

situp = random.randint(1,8)
radio.send("RNDM_SNSR-" + str(situp))
display.show(str(situp))
print(situp)

while True:
    msg = radio.receive()
    if msg:
        if msg == "SNSR_RNDM-1":
            music.play(music.ODE, wait=False)
            control = random.randint(1,9)
            radio.send("RNDM_INPT-" + str(control))
            display.show(str(control))
        elif msg == "INPT_RNDM-1":
            situp = random.randint(1,8)
            radio.send("RNDM_SNSR-" + str(situp))
            display.show(str(situp))