# Pull it
# https://trello.com/c/3lagC1Oo
import radio

class Client:
	"""Sends trigger messages to a server on the same channel"""
	def __init__(self, chan, name):
		self.channel = chan
		self.name = name.lower()
		radio.on()
		radio.config(channel = self.channel)
		#print("Configured Client")

	def send_trigger(self):
		message = self.name
		message += ":"
		message += "triggered"
		radio.send(message)
		#print("Sent: " + message)

	def send_alive(self):
		message = self.name
		message += ":"
		message += "alive"
		#print("Sent: " + message)