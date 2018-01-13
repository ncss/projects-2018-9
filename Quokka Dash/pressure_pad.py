from microbit import *
import radio
radio.on()
radio.config(channel=62)

mid_touched = False

while True:
    if pin1.read_digital() and not mid_touched:
        display.scroll('Keep going!', wait=False)
        radio.config(channel=62)
        radio.send('mid')
        mid_touched = True

    elif pin0.read_digital() and mid_touched:
        radio.config(channel=62)
        radio.send('stop')
        radio.config(channel=72)
        radio.send('stop')
        display.show(Image.HAPPY)
        sleep(5000)
        display.scroll("You Won!")

        # Restart program
        mid_touched = False
        display.show(Image.SAD)
