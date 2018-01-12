from microbit import *
import neopixel

npix = neopixel.NeoPixel(pin0, 10)
RAINBOW = [(255,0,0),(255,140,0),(255,255,0),(0,255,162),(0,128,0),(0,0,255),(145,0,255),(75,0,130),(255,130,238),(0,0,0)]


def rainbow():
    n = 0
    while True:
        for pix in range(len(npix)):
            npix[(pix+n)%len(npix)] = RAINBOW[pix%len(RAINBOW)]
        npix.show()
        n += 1
        sleep(100)
        
rainbow()
