from microbit import *
import speech
import radio
import music

radio.on()
radio.config(channel = 69)

sounds = {'bop_it': 'Bop- it?', 'pull_it': 'Pull- it?', 'twist_it': 'Twist- it?', 'shake_it': 'Shake- it?', 
'spin_it': 'Spin- it?', 'shout_it': 'Shout- it?'}

SPEED = 20

while True:
    sound_to_play = radio.receive()
    if sound_to_play:
        module, is_module = sound_to_play.split(':')
        if is_module == 'is_module' and module in sounds:
            speech.say(sounds[module], speed = 50)
        elif module == 'score':
            if is_module == 'lose':
                music.play(music.WAWAWAWAA)
            else:
                speech.say(is_module)
