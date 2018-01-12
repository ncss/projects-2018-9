# server
from microbit import *
import radio

class Server:
	"""docstring for Server"""
	def __init__(self, chan):
		self.channel = chan
		modules = {}
		radio.configure(channel = self.channel)

	def update():
		mesage = radio.receive().split(":")
		module = message[0]
		action = message[1]
		if message:
			modules.update({module, True}) # add module

	def get_module_was_triggered(module):
		if module in modules:
			state = modules[module]
			modules[module] = False
		else:
			state = False
		return state