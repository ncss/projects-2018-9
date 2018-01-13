from quokka import *
import drivers.tm1637
from machine import Pin
tm = drivers.tm1637.TM1637(clk=Pin('X9'), dio=Pin('X10'))

#timer
TIMER_LENGTH_SECS = 45
end_button = False
while True:
    if buttons.a.was_pressed():
        end_button = False
        start_time = running_time()
        end_time = start_time + TIMER_LENGTH_SECS*1000
        while running_time() < end_time and end_button == False:
            remaining_time = (end_time - running_time())//1000
            tm.numbers(*divmod(remaining_time, 60))
            if buttons.d.was_pressed():
                end_button = True
# * means unpack tuple
