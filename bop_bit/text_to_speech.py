from microbit import *
import speech
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


sounds = {'Bop it': 'Bop- it?', 'Pull it': 'Pull- it?', 'Twist it': 'Twist- it?', 'Shake it': 'Shake- it?', 
'Spin it': 'Spin- it?', 'Shout it': 'Shout- it?'}

SPEED = 20

while True:
    sound_to_play = radio.receive()
speech.say('Shake- it?')
speech.say('Bop- it?')
speech.say('Pull- it?')
speech.say('Twist- it?')
speech.say('Spin- it?')
speech.say('Shout- it?')
display.clear()