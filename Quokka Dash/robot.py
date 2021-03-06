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

def amap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return "Vector, x:{} y:{}".format(self.x, self.y)
    @classmethod
    def mag(cls, vect):
        return (vect.x ** 2 + vect.y ** 2) ** 0.5

def constrain(x, min_x, max_x):
    return max(min(max_x, x), min_x)
    
class Robot:
    MAX_SPEED = 0.6
    
    
    def __init__(self, left_motor_pins, right_motor_pins):
        self.leftH, self.leftL = left_motor_pins
        self.rightH, self.rightL = right_motor_pins

    def motors(self, left_speed, right_speed):
        self.control(self.leftH, self.leftL, left_speed)
        self.control(self.rightH, self.rightL, right_speed)
        
    def control(self, pinH, pinL, speed):
        if speed > 0:
            pinH.write_analog(abs(speed) * 1023)
            pinL.write_digital(0)
        else:
            pinH.write_digital(0)
            pinL.write_analog(abs(speed) * 1023)

class Controller:
    MAX_SPEED = 1
    DELAY = 1000
    
    def __init__(self, robot):
        self.robot = robot
        self.left_speed = 0
        self.right_speed = 0
        self.left_update = 0
        self.right_update = 0
        
    def update(self):
        msg = radio.receive()
        if msg:
            if msg == 'stop':
                return True
            try:
                wheel, speed = msg.split(':')
            except:
                return
            speed = int(speed)
            if wheel == 'L':
                self.left_speed = amap(speed, 0, 100, 0, Controller.MAX_SPEED)
                if speed > 0:
                    self.left_update = running_time()
            
                
            elif wheel == 'R':
                self.right_speed = amap(speed, 0, 100, 0, Controller.MAX_SPEED)
                if speed > 0:
                    self.right_update = running_time()
                    
        if running_time() - self.left_update > Controller.DELAY:
            self.left_speed = -0.3
        if running_time() - self.right_update > Controller.DELAY:
            self.right_speed = -0.3
        print(self.left_speed, self.right_speed)
        self.robot.motors(self.left_speed, self.right_speed)
        
        
thing = Robot([pin16, pin0], [pin12, pin8])
person = Controller(thing)

while True:
    thing.motors(0, 0)
    radio.config(channel = start_channel)
    
    while True:
        msg = radio.receive()
        if msg == 'start':
            radio.config(channel=game_channel)
            break

    for i in range(5):
        display.show(FLASH[i])
        sleep(100)
    display.clear()
    
    left_update = running_time()
    right_update = running_time()
    
    while True:
        if person.update():
            break
