from microbit import *
import neopixel
import radio

radio.on()
radio.config(channel = 69)

scores = [
    ("red", 0),
    ("green", 0),
    ("blue", 0),
    ("magenta", 0),
    ("cyan", 0),
    ("yellow", 0),
]

colors = {
    "red" : (255, 0, 0),
    "green" : (0, 255, 0),
    "blue" : (0, 0, 255),
    "magenta" : (255, 0, 255),
    "cyan" : (0, 255, 255),
    "yellow" : (255, 255, 0),
}

while True:
    msg = radio.receive()
    if msg:
        msg = msg.split(":")
        if msg[0] == "score":
            if msg[1] = "new_game":
                # move to different color
            elif:
                # set current color to score
                # then display 