from microbit import *
import neopixel
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
        
# each person gets a 4-character name, top 3 shown
leaderboard_scores = [(0, 'n'), (0, 'n'), (0, 'n')]

sc = input('What is the number? ')

while sc:
    sc = tuple((int(sc.split(', ')[0]), (sc.split(', ')[1])[:4]))
    leaderboard_scores.append(sc)
    leaderboard_scores = sorted(leaderboard_scores, key=lambda score_tuple: score_tuple[0], reverse=True)[:-1]
    sc = input('What is the number? ')



