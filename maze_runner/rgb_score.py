from microbit import *
import radio

radio.on()
score_current = 0

while True:
    score_update = int(radio.receive())
    if score_update and score_update:
        score_current += score_update
    display.show(str(score_update))