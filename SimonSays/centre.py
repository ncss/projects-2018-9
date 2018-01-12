from microbit import *
import radio

radio.on()

start_button = button_a #Change for whatever button it is configured to

radio.config(channel=73, group=2) #Configures to radio to use its own channel to prevent noise

units = [] #Units start as empty
in_game = False
def setup():
    print("Setting up device")
    unit_name = "unit%d" % len(units) #%d means that "%d" will be replaced with the length of units (the "d" is the type)
    print(unit_name)
    radio.send("setup:" + unit_name)
    units.append(unit_name)

colours = ["red", "green", "blue", "yellow"] #Interpreted by clients

def new_game():
    radio.send("newgame") #Client receives this and resets variables (possibly)
    for index, element in  enumerate(units): #Send a colour to each unit
        radio.send("%s:%s" % (element, colours[index])) #"unit3:blue"
    
while True:
    if radio.receive() == 'requestname' and not in_game:
        setup()
        
        
    if not in_game and start_button.was_pressed():
        new_game()
        in_game = True
    