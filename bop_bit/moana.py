from microbit import *
import music

music.set_tempo(bpm=88)

""" I've been staring at the edge of the water long as I can remember, 
never really knowing why."""

staring_at_the_edge = ['e4:3', 'b3:1', 'b3:2', 'e4:3', 'b3:1', 'e4:1', 'b3:1', 
'e4:2', 'e4:1', 'b3:1', 'f#4:3', 'c#4:3', 'f#4:3', 'c#4:3', 'f#4:2', 'e4:1',
'f#4:1', 'g#4:3', 'g#4:3', 'g#4:2', 'g#4:2', 'g#4:1', 'f#4:1', 'e4:1', 
'd#4:1', 'c#4:4', 'r:12']

""" I wish, I could be the perfect daughter, but I come back to the water
no matter how hard I try."""

perfect_daughter = ['e4:3', 'b3:5', 'r:2', 'e4:1', 'b3:1', 'e4:1', 'b3:1', 
'e4:1', 'b3:1', 'f#4:3', 'c#4:3', 'f#4:1', 'e4:1', 'f#4:2', 'f#4:2',
'f#4:1', 'e4:1', 'g#4:3', 'g#4:1', 'r:3', 'c#4:1', 'g#4:1', 'g#4:1',
'g#4:2', 'g#4:2', 'e4:2', 'e4:4', 'r:10']

""" Every turn I take, every trail I track, every path I make, every road
leads back to the place I know where I cannot go, where I long to be"""

every_turn = ['c#4:1', 'b3:1', 'c#4:2', 'e4:2', 'e4:2', 'c#4:1', 'b3:1',
'c#4:2' ,'e4:2', 'e4:2', 'c#4:1', 'b3:1', 'c#4:2', 'f#4:2', 'f#4:2', 
'c#4:1', 'b3:1', 'c#4:2', 'f#4:2', 'f#4:2', 'r:1',
'e4:1', 'e4:1', 'e4:2', 'g#4:2', 'g#4:2', 'e4:1', 'c#4:1', 'e4:2', 'g#4:2',
'g#4:2', 'f#4:1', 'g#4:1', 'a4:3', 'e4:1', 'e4:4', 'c:4', 'r:2']

""" See the line where the sky meets the sea, it calls me, and no one
knows how far it goes. """

see_the_line = ['e4:2', 'f#4:2', 'g#4:2', 'e4:1', 'f#4:1', 'g#4:2', 'e4:1',
'f#4:1', 'g#4:4', 'e4:2', 'b4:2', 'f#4:2', 'f#4:6', 'r:3', 'b3:1', 'b4:1',
'c#5:3', 'g#4:6', 'f#4:2', 'b3:1', 'b4:1', 'c#5:3','g#4:6', 'f#4:2',
'f#4:4', 'r:2']

""" If the wind in my sail on the sea stays behind me,
one day i'll know, If i go there's just no telling how far I'll go """

if_the_wind = ['e4:1', 'f#4:1', 'g#4:2', 'e4:1', 'f#4:1', 'g#4:2', 'e4:1', 
'f#4:1', 'g#4:2', 'e4:2', 'e4:2', 'b4:2', 'f#4:2', 'f#4:6', 'r:2', 'b3:2',
'b4:1', 'c#5:3', 'g#4:6', 'f#4:2', 'f#4:4', 'r:2']

music.play(staring_at_the_edge)
music.play(perfect_daughter)
music.play(every_turn)
music.play(see_the_line)