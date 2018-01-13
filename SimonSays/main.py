from quokka import *
import random

radio.enable()

start_button = buttons.a #Change for whatever button it is configured to

radio.config(channel=73) #Configures to radio to use its own channel to prevent noise

colours = ["red", "green", "blue", "yellow"] #Interpreted by clients
units = [] #Units start as empty
unit_colours = {}

rgb_colors = {"red": (255,0,0),
"green": (0,255,0),
"blue": (0,0,255),
"yellow": (255,255,0)
}



def setup():
    unit_name = "unit%d" % len(units) #%d means that "%d" will be replaced with the length of units (the "d" is the type)
    
    radio.send("%s:setup:1" % unit_name)
    units.append(unit_name)

def flash_sequence(sequence):
    print("START")
    print(sequence)
    for i in sequence:
        colour = unit_colours[i]
        print(i)
        print(colour)
        neopixels.set_pixel(1, 0, 255, 0)
        for i in range(8):
            r = rgb_colors[colour][0]
            g = rgb_colors[colour][1]
            b = rgb_colors[colour][2]
            neopixels.set_pixel(i, r, g, b)
        neopixels.show()
        sleep(1000)
        neopixels.clear()
        neopixels.show()
        sleep(250)
  
    print("END")
def shuffle(sequence):
    
    for i in range(len(sequence) - 1, 0, -1):
        j = random.randrange(0, len(sequence))
        
        [sequence[i], sequence[j]] = [sequence[j], sequence[i]];
    return sequence
        
    
    
def new_game():

    radio.send("all:new_game:1") #Client receives this and resets variables (possibly)
    
    colour_list = shuffle(colours)
    
    for index, element in  enumerate(units): #Send a colour to each unit
        print("%s:colour:%s" % (element, colour_list[index]))
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
    print("Should reset")
    progress = 0
    start = 0
    end = 0
    round_count = 0
    in_game = False
    in_round = False
    round_limit = 3
    should_show_units = True
    total_time = 0
    sequence_length = 3

    pass
    
progress = 0
start = 0
end = 0
round_count = 0
in_game = False
in_round = False
round_limit = 3
should_show_units = True
total_time = 0
sequence_length = 3

while True:
    pressed = start_button.was_pressed()
    pressed_d = buttons.d.was_pressed()

    if pressed_d:
        print("Let's go")
        new_game()
        progress = 0
        start = 0
        end = 0
        round_count = 0
        in_game = False
        in_round = False
        round_limit = 3
        should_show_units = True
        total_time = 0
        sequence_length = 3

    if not in_game and should_show_units:
        display.fill(0)
        display.text(str(len(units)), 5, 5, 1, scale=8) # second last argument is colour
        display.show()
        sleep(100)

    if not in_round and pressed:
        display.fill(0)
        display.show()
        radio.send("all:new_round:1")
        print("HERE")
        round_count += 1
        sequence = generate_sequence(sequence_length)
        sequence_length += 2

        print(sequence)
        progress = 0
        in_game = True
        in_round = True

        flash_sequence(sequence) #Start timer after flashing sequence
        start = running_time()
    try:
        receive = radio.receive()
    except:
        receive = None
        
    if not receive:
        continue
    receive = receive.split(":")
    
    if receive[0] == 'requestname' and not in_game:
        setup()
        continue
    #PROTOCOL STARTS
    if len(receive) != 3:
        continue
    print(receive)
    unit = receive[0]
    instruction = receive[1]
    data = receive[2]
    
    if instruction == "pressed" and int(data):
        print("here")
        if unit == sequence[progress]:
            print("Corecct")
            progress += 1
            radio.send("%s:correct:1" % unit)
            print("Progress %d" % progress)
            print(len(sequence))
            if progress == len(sequence): #Finished Round
                radio.send("all:round_finished:1")
                end = running_time()
                total_time += (end - start)
                print(total_time)

                if round_count >= round_limit:
                   

                    should_show_units = False
                    display.fill(0)

                    display.text("{0:.1f}".format(total_time / 1000) + "s", 5, 5, 1, scale=2) # second last argument is colour
                    display.text("Woohoo!", 5, 30, 1, scale=2)
                    display.show()
                    in_round = False
                    in_game = False
                else:
                    
                    in_round = False
        else:
            print("Pressed %s, should've pressed %s" %(unit, sequence[progress]))
            radio.send("all:incorrect:1")

            #oh no it's wrong
    #unit1:pressed:1
    
    
        
     