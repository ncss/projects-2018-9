from microbit import *
import radio
radio.on()
radio.config(channel=62)

while True:
    if button_a.was_pressed():
        display.scroll("Stop")
        radio.config(channel=72)
        radio.send("stop")
        radio.config(channel=62)
        radio.send("stop")
    if button_b.was_pressed():
        radio.send("start")
        display.scroll("Start")
        