Simon Says

Components:
4x microbits(minimimum)
1x Quokka
5x Neopixels
10x Buttons(Preferably big red button at centre)
Lots of Cables

Radio messages sent by Centre(Quokka):
"all:newgame:1"
"%s:setup:1" % unit_name                         #Example: unit1:setup:1	
"%s:colour:%s" % (element, colour_list[index])   #Example: unit2:colour:blue
"all:round_finished:1"
"%s:correct:0" % unit                            #Example: unit3:correct:0
 

Radio messages sent by Units(Microbits):
unit_name + ":pressed:1"                         #Example: unit2:pressed:1
"requestname"
unit_name + ":pressed:1"                         #Example: unit2:pressed:1

Radio Channel: 73

Protocols:
unit#:instruction:data

