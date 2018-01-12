# Bop it
# https://trello.com/c/vSm7z3AP

from microbit import *
import server

server = Server(69)

debug = False

def is_triggered():
	pressed = pin0.read_digital()
	if pressed == 0:
		if debug: print('yes')
		return True
    else:
		if debug: print('no')
		return False

while True:
	server.set_module_was_triggered("bop_it")
