from microbit import *
import radio

radio.on()

radio.config(channel=73, group="ncssgroup2") #Configures to radio to use its own channel to prevent noise

units = [] #Units start as empty
in_game = False
def setup():
    
    

    


