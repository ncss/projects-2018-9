from microbit import *
import radio
radio.on()
radio.config(channel=62)

while True:
    if pin1.read_digital():
        radio.send('Half')
        display.scroll('!Keep Going!')
    elif pin0.read_digital():
        radio.send('Done')
        radio.config(channel=72)
        radio.send('Stop')
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
