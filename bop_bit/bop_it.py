# Bop it
# https://trello.com/c/vSm7z3AP

from microbit import *
import random
import radio

class Server:
    """docstring for Server"""
    def __init__(self, chan):
        self.channel = chan
        self.modules = {"bop_it": False}
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
            #print(self.modules)
        else:
            state = False
        return state

    def set_module_was_triggered(self, module):
        self.modules[module] = True

server = Server(69)

debug = True

pin0.set_pull(pin0.PULL_UP)
pressed_last_state = False
def is_triggered(prev_state):
    state = pin0.read_digital()
    if state and not prev_state:
        return True, state
    else:
        return False, state

""" GAME STUFF """

sleep(1000)
score = 0
lives = 3
timeout = 3 * 1000
speed = 0
trigger_last = False
radio.send("score:new_game")

while True:       
    module_current = random.choice(list(server.modules.keys()))
    radio.send(module_current + ":is_module") # e.g. "bop_it:is_module"
    begin_time = running_time()
    while True:
        if (running_time() - begin_time) >= (timeout - speed):
            if lives <= 0:
                print("die!")
                break
            else:
                print("lose!")
                lives -= 1
            break
        else:
            trigger = pin0.read_digital()
            if trigger and not trigger_last:
                print("bopped")
                server.set_module_was_triggered("bop_it")
            trigger_last = trigger
            
            if server.get_module_was_triggered(module_current):
                print("win!")
                score += 1
                speed += 1
                radio.send("score:" + str(score))
                break

