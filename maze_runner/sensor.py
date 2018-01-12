from microbit import *
import radio

prev = accelerometer.current_gesture()
curr = prev
radio.on()
radio.config(channel=71)
while True:
    temp = accelerometer.current_gesture()
    
    if temp:
        curr = temp
    
    if curr == "up" and prev == "face up":
        print("sitting up")
    
    prev = curr