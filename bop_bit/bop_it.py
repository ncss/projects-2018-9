# Bop it
# https://trello.com/c/vSm7z3AP

from microbit import *
import random
import radio

class Server:
    """docstring for Server"""
    def __init__(self, chan):
        self.channel = chan
        self.modules = {}
        radio.on()
        radio.config(channel = self.channel)

    def update(self):
        message = radio.receive()
        if message:
            module, action = message.split(":")
            self.modules[module] = True # add module

    def get_module_was_triggered(self, module):
        if module in self.modules:
            state = self.modules[module]
            self.modules[module] = False
        else:
            state = False
        return state

    def set_module_was_triggered(self, module):
        if module in self.modules:
            modules[module] = True

server = Server(69)

debug = True

def is_triggered():
    pressed = pin0.read_digital()
    if pressed == 0:
        return True
    else:
        return False

""" GAME STUFF """

def set_to_default_game_state():
    if debug: print("set_to_default_game_state")
    timeout = 5000
    module_current = ""
    lives = 3
    begin_time = running_time()
    score = 0
    speed = 0

def pick_next_module():
    if debug: print("pick_next_module")
    module_current = random.choice(server.modules)
    begin_time = running_time()
    # say module with text to speech

while True:
    while not is_triggered():
        # start game!
        set_to_default_game_state()
        pick_next_module()
        while True:
            # check timeout
            if (running_time() - begin_time) >= (timeout - speed):
                # ran out of time!
                if (lives <= 0):
                    # die
                    # play bad sound
                    # incomplete
                    sleep(5000)
                    break # go back to waiting for button press
                else:
                    lives -= 1 # remove a life
                continue

            if is_triggered():
                server.set_module_was_triggered("bop_it")
            
            if server.get_module_was_triggered(module_current):
                if debug: print("module_was_triggered")
                # yay! go to next
                score += 1 # incriment score
                # increase speed
                if speed > 1000:
                    speed += 10
                # pick next module
                pick_next_module()
                continue
