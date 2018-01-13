from microbit import *
import radio
radio.on()
radio.config(channel=62)
# assign colour names to each of the pins
red = pin13
green = pin0

#variable timer in seconds * 1024 (to make life easier) :D
seconds = 37
time_ms = seconds * 1000

num_of_colours = 1024
#while True:
    #decreasing time fraction
u = 0
d = 0
listen = True
start = running_time()
while True:
    while listen:
        rado = radio.receive()
        if rado == "start":
           listen = False
           
    for up, down in zip(range(num_of_colours), range(num_of_colours-1, 0, -1)):
        green.write_analog(down)
        red.write_analog(up)
        u = up
        d = down
        sleep(time_ms/num_of_colours)
        rado = radio.receive()
        if rado == "done":
            break
            finish = True:
    print("mark")
    x = 1000
    if finish != True:
        while x > 5:
            red.write_analog(0)
            print(x)
            sleep(x)
            red.write_analog(1023)
            sleep(x)
            x = x//1.5
    finish = False
    end = running_time()
    red.write_analog(0)
    green.write_analog(0)
    print((end-start)//1000)
