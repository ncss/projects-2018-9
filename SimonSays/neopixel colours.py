from microbit import *
import neopixel

npix = neopixel.NeoPixel(pin0, 7)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

def LightAll(col):
    for pix in range(0, len(npix)):
        npix[pix] = col
    npix.show()
    return

while True:
    LightAll(red)
    sleep(5000)
    LightAll(green)
    sleep(5000)
    LightAll(blue)
    sleep(5000)
    LightAll(yellow)
    sleep(5000)
    
    
    