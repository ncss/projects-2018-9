from microbit import *
import radio
import random
import math

radio.on()

start_button = button_a #Change for whatever button it is configured to

radio.config(channel=73, group=2) #Configures to radio to use its own channel to prevent noise

colours = ["red", "green", "blue", "yellow"] #Interpreted by clients
units = [] #Units start as empty
unit_colours = {}


in_round = False
def setup():
    print("Setting up device")
    unit_name = "unit%d" % len(units) #%d means that "%d" will be replaced with the length of units (the "d" is the type)
    print(unit_name)
    
    radio.send("%s:setup:1" % unit_name)
    units.append(unit_name)

def flash_sequence(sequence):
    for i in sequence:
        #colour = (unit_colours[i])
        #flashing code
        #sleep(500)
        pass
def shuffle(sequence):
    
    for i in range(len(sequence) - 1, 0, -1):
        j = random.randrange(0, len(sequence))
        
        [sequence[i], sequence[j]] = [sequence[j], sequence[i]];
    return sequence
        
    
    
def new_game():
    radio.send("all:newgame:1") #Client receives this and resets variables (possibly)
    
    colour_list = shuffle(colours)
    
    for index, element in  enumerate(units): #Send a colour to each unit
    
        radio.send("%s:colour:%s" % (element, colour_list[index])) #"unit3:color:blue"
        unit_colours[element] = colour_list[index]
    
    print(unit_colours)

def generate_sequence(sequence_length):
    sequence = []
    for i in range(sequence_length):
        sequence.append(random.choice(units))
    return sequence

def round_finished():
    print("do later")


def reset_game():
    print("Delete everything")
    reset()
progress = 0
sequence = []

while True:
    
    if not in_round and start_button.was_pressed():
        new_game()
        sequence = generate_sequence(3)
        in_round = True
    
    display.show(str(len(units)))
    
    receive = radio.receive()
    if not receive:
        continue
    receive = receive.split(":")
    
    if receive[0] == 'requestname' and not in_round:
        setup()
        continue
    #PROTOCOL STARTS
    if len(receive) != 3:
        continue
    print(receive)
    unit = receive[0]
    instruction = receive[1]
    data = receive[2]
    
    if instruction == "clicked" and int(data):
        if unit == sequence[progress]:
            #correct
            progress += 1
            radio.send("%s:correct:1" % unit)
            if progress == len(sequence):
                radio.send("all:round_finished:1")
        else:
            print("ughhhh")
            radio.send("%s:correct:0" % unit)
            reset_game()
            #oh no it's wrong
    #unit1:pressed:1
    
    
        
     