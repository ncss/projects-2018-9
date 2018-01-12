from microbit import *
import radio
radio.on()
ID = "L:"

control = 0
control_values = 0
num = 100
for i in range(num):
    cont_y = accelerometer.get_y()
    control_values += cont_y
    sleep(20)
control = control_values/100
print(control)

def check():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print("x, y, z:", x, y, z)
count = 1
jumps = 0
while True:
    y = accelerometer.get_y()
    y_base = y-control
    #check()
    if abs(y_base) > 1000:
        y_base = 1000
    if abs(y_base) > 900:
        percent = abs(y_base)/10
        print(str(percent)+" percent")
    if count == 16:
        radio.send("L: "+jumps)
        count = 1
        jumps = 0
    #if y > 1000:
        #print("jumped")
    #else:
        #print("still")
    count += 1
    sleep(125)
