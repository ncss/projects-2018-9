from microbit import *
import radio
radio.on()
radio.config(channel=62)

while True:
    if pin1.read_digital():
        display.scroll('!Keep Going!')
        radio.send('Half')
    elif pin0.read_digital():
        display.show(Image.HAPPY)
        radio.send('Done')
        radio.config(channel=72)
        radio.send('Stop')
    else:
        display.show(Image.SAD)
