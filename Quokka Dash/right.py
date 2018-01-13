from microbit import *
import radio

start_channel = 62
game_channel = 72

FLASH = [
  Image('99999:99999:99999:99999:99999'),
  Image('77777:77777:77777:77777:77777'),
  Image('55555:55555:55555:55555:55555'),
  Image('33333:33333:33333:33333:33333'),
  Image('11111:11111:11111:11111:11111')
]

radio.on()

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
    radio.config(channel = start_channel)
    display.show('R')
    while True:
        msg = radio.receive()
        if msg == 'start':
            radio.config(channel=game_channel)
            break

    for i in range(5):
        display.show(FLASH[i])
        sleep(100)
    display.clear()
      
    display.show(Image.HAPPY)
    while True:
        msg = radio.receive()
        if msg == 'stop':
            break
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
