from quokka import *
import drivers.tm1637
#from machine import Pin
from machine import *
radio.config(channel=62)
radio.enable()

'''
while True:
    msg = radio.receive()
    if msg:
        display.fill(1)
        display.text(msg, 5, 5, 0)
        display.show()
    if buttons.a.was_pressed():
      radio.send('a')
'''

tm = drivers.tm1637.TM1637(clk=Pin('X9'), dio=Pin('X10'))

while True:
    #timer
    TIMER_LENGTH_SECS = 45
    end_button = False
    while True:
        if groves.d.pin0.read_digital():
            end_button = False
            radio.send('start')
            start_time = running_time()
            end_time = start_time + TIMER_LENGTH_SECS*1000
            while running_time() < end_time and end_button == False:
                remaining_time = (end_time - running_time())//1000
                tm.numbers(*divmod(remaining_time, 60))
                if groves.c.pin0.read_digital() or radio.receive() == "stop":
                    end_button = True
    # * means unpack tuple


'''
while True:
    start buttons
    send signal to all to begin
    wait for the end signal
    repeat
'''
