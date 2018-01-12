# server
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