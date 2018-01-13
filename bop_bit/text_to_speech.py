from microbit import *
import speech
import radio
import music


sounds = {'bop_it': 'Bop- it?', 'twist_it': 'Twist- it?', 'shake_it': 'Shake- it?', 
'spin_it': 'Spin- it?', 'shout_it': 'Shout- it?'}

SPEED = 20
radio.on()
radio.config(channel=69)
current_score = 0

while True:
    sound_to_play = radio.receive()
    if sound_to_play:
        module, is_module = sound_to_play.split(':')
        if is_module == 'is_module' and module in sounds:
            speech.say(sounds[module], speed = 50)
        elif is_module =='lose':
            music.play(music.WAWAWAWAA)
    """
    score = radio.receive()
    if score and ':' in score:
        a, sc = score.split(':')
        if a == 'score':
            if sc == 'lose':
                music.play(music.WAWAWAWAA)
            elif sc in '0123456789' and int(sc) > current_score:
                music.play(music.BA_DING)
                current_score = int(sc)
        elif a == 'speed':
            music.play(JUMP_DOWN)
        elif sc == 'is_module' and a in sounds:
            speech.say(sounds[a], speed = 50)
    """
