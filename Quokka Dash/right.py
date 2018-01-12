from microbit import *
import radio
radio.on()
radio.config(channel=72)
ID = "R:"

control = 0
control_values = 0
num = 100
for i in range(num):
    cont_y = accelerometer.get_y()
    control_values += cont_y
    sleep(20)
control = control_values/100
print(control)
display.show(Image.HAPPY)
def check():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print("x, y, z:", x, y, z)
count = 1
jump = 0
jumps = [0]
final = 0
while True:
    y = accelerometer.get_y()
    y_base = y-control
    #check()
    if abs(y_base) > 1000:
        y_base = 1000
    if abs(y_base) > 950:
        percent = abs(y_base)/10
        jumps.append(1)
    else:
        jumps.append(0)
    while len(jumps) > 15:
        jumps.pop(0)
        
    prin = ID+str(int(sum(jumps)/len(jumps)*100))
    radio.send(prin)
    print(prin)
    count += 1
    sleep(25)
