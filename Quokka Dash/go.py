from microbit import *
import radio
radio.on()
radio.config(channel=62)
display.off()

red1 = pin3
green1 = pin2
red2 = pin0
green2 = pin1

red1.write_digital(0)
green1.write_digital(0)
red2.write_digital(0)
green2.write_digital(0)
    
def colors():
    red1.write_analog(1000)
    green1.write_analog(0)
    red2.write_analog(1000)
    green2.write_analog(0)
    sleep(500)
    red1.write_digital(0)
    green1.write_digital(0)
    red2.write_digital(0)
    green2.write_digital(0)
    sleep(500)
    red1.write_analog(700)
    green1.write_analog(300)
    red2.write_analog(700)
    green2.write_analog(300)
    sleep(500)
    red1.write_digital(0)
    green1.write_digital(0)
    red2.write_digital(0)
    green2.write_digital(0)
    sleep(500)
    red1.write_analog(0)
    green1.write_analog(1000)
    red2.write_analog(0)
    green2.write_analog(1000)
    sleep(1000)
    red1.write_digital(0)
    green1.write_digital(0)
    red2.write_digital(0)
    green2.write_digital(0)

listen = True
wait = True
while True:
    while listen:
        rado = radio.receive()
        if rado == "start":
           listen = False
    while listen == False:
        if wait:
            colors()
        wait = False
        rado = radio.receive()
        if rado == "mid":
            green1.write_digital(1)
            green2.write_digital(0)
        if rado == "stop":
            listen = True
            
        