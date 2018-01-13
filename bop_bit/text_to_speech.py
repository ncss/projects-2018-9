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


sounds = {'bop_it': 'Bop- it?', 'pull_it': 'Pull- it?', 'twist_it': 'Twist- it?', 'shake_it': 'Shake- it?', 
'spin_it': 'Spin- it?', 'shout_it': 'Shout- it?'}

SPEED = 20

while True:
    sound_to_play = radio.receive()
    if sound_to_play:
        sound_to_play.split(':')
        if sound_to_play[1] == 'is_module':
            speech.say(sounds[sound_to_play[0]]
