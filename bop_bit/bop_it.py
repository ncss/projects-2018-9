# Bop it
# https://trello.com/c/vSm7z3AP

from microbit import *
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
	# this
	if is_triggered():
		server.set_module_was_triggered("bop_it")
