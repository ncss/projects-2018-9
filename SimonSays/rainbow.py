from microbit import *
import neopixel

npix = neopixel.NeoPixel(pin0, 10)
RAINBOW = [(128,0,0),(128,70,0),(128,128,0),(0,128,81),(0,64,0),(0,0,128),(75,0,128),(35,0,65),(128,65,170),(0,0,0)] #half brightness colours


def rainbow():
    n = 0
    while True:
        for pix in range(len(npix)):
            npix[(pix+n)%len(npix)] = RAINBOW[pix%len(RAINBOW)]
        npix.show()
        n += 1
        sleep(100)
        
rainbow()
