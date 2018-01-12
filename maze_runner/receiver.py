from microbit import *

while True:
    g = accelerometer.current_gesture()
    if g:
        print(g)
    