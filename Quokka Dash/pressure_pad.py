from microbit import *
import radio
radio.on()
radio.config(channel=62)

while True:
    if pin1.read_digital():
        radio.send('mid')
        display.scroll('!Keep Going!')
    elif pin0.read_digital():
        radio.send('done')
        radio.config(channel=72)
        radio.send('stop')
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
