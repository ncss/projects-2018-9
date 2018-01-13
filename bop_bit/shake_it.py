# Shake it
# https://trello.com/c/5Buph40r
from microbit import *
import radio
display.show(Image.ALL_CLOCKS, loop=True, delay=100, wait=False)

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

client = Client(69, "shake_it")

def is_triggered():
    gesture = accelerometer.was_gesture("shake")
    if gesture:
        display.show(Image.HAPPY)
        client.send_trigger()
        #print('YAY')
    else:
        display.show(Image.SAD)