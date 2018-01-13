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
'b4:1', 'c#5:3', 'g#4:6', 'f#4:2', 'f#4:4', 'r:2', 'f#4:1', 'g#4:1',
'a4:2', 'e4:2', 'e4:2', 'c4:2', 'c4:1', 'b3:2', 'b3:2', 'b3:2', 'e4:2',
'e4:2', 'r:1']

"""I know everybody on this island seems so happy on this island. Everything
is by design"""

i_know = ['b3:1', 'b3:2', 'e4:2', 'e4:2', 'e4:1', 'b3:1', 'e4:1', 'b3:1',
'e4:1', 'b3:1', 'f#4:3', 'c#4:3', 'f#4:2', 'f#4:1', 'c#4:3', 'f#4:1', 'e4:1',
'f#4:1', 'e4:1', 'g#4:3', 'g#4:5', 'g#4:1', 'g#4:1', 'g#4:1', 'g#4:1', 
'g#4:2', 'e4:1', 'e4:5', 'r:12']

""" I know everybody on this island has a role on this island, so maybe
I can roll with mine"""

roll_with = ['e4:3', 'b3:3', 'e4:3', 'b3:4', 'e4:1', 'b3:1', 'e4:1', 'b3:1',
'f#4:3', 'c#4:3', 'f#4:3', 'c#4:3', 'f#4:2', 'e4:1', 'f#4:1', 'g#4:3',
'g#4:4', 'c#4:1', 'g#4:1', 'g#4:1', 'g#4:1', 'g#4:1', 'g#4:2', 'e4:1',
'e4:5', 'r:4', 'r:6']

""" I can lead with pride, I can make us strong, I'll be satisfied if I
play along but the voice inside sings a different song. What is wrong 
with me?"""
i_can = ['c#4:1', 'b3:1', 'c#4:2', 'e4:2', 'e4:2', 'c#4:1', 'b3:1',
'c#4:2' ,'e4:2', 'e4:2', 'c#4:1', 'b3:1', 'c#4:2', 'f#4:2', 'f#4:2', 
'c#4:1', 'b3:1', 'c#4:2', 'f#4:2', 'f#4:2', 'e4:1', 'c#4:1', 'e4:2',
'g#4:2', 'g#4:2', 'e4:1', 'c#4:1', 'e4:2', 'g#4:2', 'g#4:2', 'r:1',
'b4:1', 'b4:1', 'c5:4', 'g5:4', 'g5:4', 'r:18']

""" See the light as it shines on the sea it's 
blinding but no one knows how deep it goes"""
see_the_line2 = ['e4:1', 'f#4:1', 'g#4:2', 'e4:1', 'f#4:1', 'g#4:2', 'e4:1',
'f#4:1', 'g#4:4', 'e4:2', 'b4:2', 'f#4:2', 'f#4:6', 'r:3', 'b3:1', 'b4:1',
'c#5:3', 'g#4:6', 'f#4:5', 'b3:1', 'b4:1', 'c#5:3','g#4:6', 'f#4:2',
'f#4:4', 'r:2', ]

""" And it seems like it's calling out to me, so come find me and let
me know. """
and_it_seems = ['e4:1', 'f#4:1', 'g#4:2', 'e4:2', 'e4:2', 'e4:1',
]

while True:
    music.play(staring_at_the_edge)
    music.play(perfect_daughter)
    music.play(every_turn)
    music.play(see_the_line)
    music.play(if_the_wind)
    music.play(i_know)
    music.play(roll_with)
    music.play(i_can)
    music.play(see_the_line2)