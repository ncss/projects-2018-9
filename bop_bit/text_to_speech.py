from microbit import *
import speech
import radio

radio.on()
radio.config(channel = 69)

sounds = {'bop_it': 'Bop- it?', 'pull_it': 'Pull- it?', 'twist_it': 'Twist- it?', 'shake_it': 'Shake- it?', 
'spin_it': 'Spin- it?', 'shout_it': 'Shout- it?'}

SPEED = 20

while True:
    sound_to_play = radio.receive()
    if sound_to_play:
        sound_to_play.split(':')
        if sound_to_play[1] == 'is_module' and sound_to_play[0] in sounds:
            speech.say(sounds[sound_to_play[0]])
