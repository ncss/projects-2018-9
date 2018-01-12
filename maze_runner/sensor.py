from microbit import *
import radio

situps_left = 0
prev = accelerometer.current_gesture()
curr = prev
radio.on()
radio.config(channel=71)
while True:
    if situps_left:
        display.show(str(situps_left))
        temp = accelerometer.current_gesture()
        
        if temp:
            curr = temp
        
        if curr == "up" and prev == "face up":
            print("sitting up")
            situps_left -= 1
        
        display.show(str(situps_left))
        
        if not situps_left:
            radio.send("SNSR_RNDM-1")
            display.show(Image.HAPPY)
        
        prev = curr
        
    else:
        msg = radio.receive()
        if msg and msg.startswith("RNDM_SNSR-"):
            situps_left = int(msg[10])
            print(str(situps_left))