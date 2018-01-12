from microbit import *
import radio 

radio.on()
radio.config(channel=72)
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
    MAX_SPEED = 0.6
    DELAY = 1000
    LED_UPDATE = 10
    END_POINTS = [(0, 3), (0, 2), (1, 1), (2, 1), (3, 1), (4, 2), (4, 3)]
    
    def __init__(self, robot):
        self.robot = robot
        self.left_speed = 0
        self.right_speed = 0
        self.left_update = 0
        self.right_update = 0
        self.led_update = 0
        self.prev_leds = []
        self.led_length = 5

    def update(self):
        msg = radio.receive()
        if msg:
            wheel, speed = msg.split(':')
            speed = min(int(speed), 15)
            print(msg)
            if wheel == 'L':
                self.left_speed = amap(speed, 0, 100, 0, Controller.MAX_SPEED)
                if speed > 0:
                    self.left_update = running_time()
                
            elif wheel == 'R':
                self.right_speed = amap(speed, 0, 100, 0, Controller.MAX_SPEED)
                if speed > 0:
                    self.right_update = running_time()
                    
        if running_time() - self.left_update > Controller.DELAY:
            self.left_speed = -0.2
        if running_time() - self.right_update > Controller.DELAY:
            self.right_speed = -0.2
            
        self.robot.motors(self.left_speed, self.right_speed)
    
        if running_time() - self.led_update > Controller.LED_UPDATE:
            display.clear()
            while len(self.prev_leds) > self.led_length:
                self.prev_leds.pop(0)
            index = int(map(self.left_speed - self.right_speed, -1, 1, 0, 7) + 0.5)
            self.prev_leds.append(self.END_POINTS[index])
            print(self.prev_leds)
            for i in range(len(self.prev_leds)):
                x, y = self.prev_leds[i]
                self.draw_line(Vector(2, 3), Vector(x, y), [1, 3, 5, 7, 9][5-len(self.prev_leds) + i])
            self.led_update = running_time()
            self.led_render()
        
    def draw_line(self, start, end, brightness=9):
        if start.x == end.x:
            for y in range(start.y, end.y + [-1, 1][end.y > start.y], [-1, 1][start.y < end.y]):
                self.led_array[y][start.x] = brightness
                # display.set_pixel(start.x, y, brightness)
            return
        if start.x > end.x:
            start, end = Vector(end.x, end.y), Vector(start.x, start.y)
        m = (start.y - end.y) / (start.x - end.x)
        c = start.y - m * start.x
        length = int(Vector.mag(start - end) + 1) 
        for gap in range(length + 1):
            x = map(gap, 0, length, start.x, end.x)
            y = m * x + c
            self.led_array[constrain(int(y + 0.5), 0, 4)][constrain(int(x + 0.5), 0, 4)] = brightness
            
    def led_render(self):
        for y, row in enumerate(self.led_array):
            for x, item in enumerate(row):
                display.set_pixel(x, y, item)
                self.led_array[y][x] = 0
        
thing = Robot([pin16, pin0], [pin12, pin8])
person = Controller(thing)

while True:
    person.update()
