# client
from microbit import *
import radio

class Client:
	"""Sends trigger messages to a server on the same channel"""
	def __init__(self, chan, name):
		self.channel = chan
		self.name = name.lower()
		radio.configure(channel = self.channel)
		#print("Configured Client")

	def send_trigger():
		message += self.name
		message += ":"
		message += "triggered"
		radio.send(message)
		#print("Sent: " + message)

	def send_alive():
		message += self.name
		message += ":"
		message += "alive"
		#print("Sent: " + message)