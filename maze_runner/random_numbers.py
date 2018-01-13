from microbit import *
import radio
import random
import music
# RNDM
sit = [3,4,2,5,5,1,5,2,3,6,1,3,1,2,4,4,3,5,2,3,2,5,5,5]
ind = 1 

radio.on()
radio.config(channel=71)

situp = sit[0]
radio.send("RNDM_SNSR-" + str(situp))
display.show(str(situp))
print(situp)

while True:
    msg = radio.receive()
    if msg:
        print(msg)
        if msg == "SNSR_RNDM-1":
            music.play(music.RINGTONE, wait=False)
            control = random.randint(1,8)
            radio.send("RNDM_INPT-" + str(control))
            display.show(str(control))
            print(control)
        elif msg == "INPT_RNDM-1":
            situp = sit[ind%20]
            ind += 1
            radio.send("RNDM_SNSR-" + str(situp))
            display.show(str(situp))
