from microbit import *
import neopixel
import radio

radio.on()
radio.config(channel=73)
unit_num = #insert num
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
    msg = radio.receive() #unit1:red EXAMPLE
    if msg.startswith(unit_num):
        colour = msg.split(':')[1]
        LightAll(colour)
        sleep(5000)
        npix.clear()
        break
    
    
    