from quokka import *
import radio

radio.on()

start_button = button_a #Change for whatever button it is configured to

radio.config(channel=73, group="ncssgroup2") #Configures to radio to use its own channel to prevent noise

units = [] #Units start as empty
in_game = False
def setup():
    unit_name = "unit%d" % len(units) #%d means that "%d" will be replaced with the length of units (the "d" is the type)
    radio.send("setup:" + unit_name)
    units.append(unit_name)
    
    
    
while True:
    if radio.recieve() == 'requestname':
        setup()
    if not in_game and start_button.read_digital():
        in_game = True
    display.show("Hey now")