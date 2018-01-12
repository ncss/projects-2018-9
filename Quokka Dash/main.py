import drivers.tm1637
from machine import Pin
tm = drivers.tm1637.TM1637(clk=Pin('X9'), dio=Pin('X10'))
tm.numbers(18, 99)
