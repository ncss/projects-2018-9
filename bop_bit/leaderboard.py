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

colors_list = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow']
current_colour_i = 0
colour = colors_list[current_colour_i]

board = neopixel.NeoPixel(pin0, 10)

while True:
    msg = radio.receive()
    if msg:
        msg = msg.split(":")
        if msg[0] == "score":
            if msg[1] = "new_game":
                current_colour_i += 1
                current_colour_i %= 6
                colour = colors_list[current_colour_i]
                # move to different color
            else:
                board[:int(msg[1])] = colors[colour]
                board.show()
                # set current color to score
                # then display 