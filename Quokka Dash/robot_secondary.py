from microbit import *
import radio

left_speed = 0
right_speed = 0
left_update = 0
right_update = 0
led_update = 0

MAX_SPEED = 0.6
DELAY = 1000
    
led_edges = [(0, 3), (0, 2), (1, 1), (2, 1), (3, 1), (4, 2), (4, 3)]
led_array = [[0 for x in range(5)] for y in range(5)]
last_points = [(2, 1)] * 5

radio.on()
radio.config(channel=72)

def amap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(x, min_x, max_x):
    return max(min(max_x, x), min_x)
    
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
        
def draw_line(start, end, brightness=9):
    if start.x == end.x:
        for y in range(start.y, end.y + [-1, 1][end.y > start.y], [-1, 1][start.y < end.y]):
            led_array[y][start.x] = brightness
            # display.set_pixel(start.x, y, brightness)
        return
    if start.x > end.x:
        start, end = Vector(end.x, end.y), Vector(start.x, start.y)
        # print(start, end)
    m = (start.y - end.y) / (start.x - end.x)
    c = start.y - m * start.x
    length = int(Vector.mag(start - end) + 1) 
    for gap in range(length + 1):
        x = amap(gap, 0, length, start.x, end.x)
        y = m * x + c
        led_array[constrain(int(y + 0.5), 0, 4)][constrain(int(x + 0.5), 0, 4)] = brightness
    
while True:
    msg = radio.receive()
    if msg:
        wheel, speed = msg.split(':')
        speed = int(speed)
        if wheel == 'L':
            left_speed = amap(speed, 0, 100, 0, MAX_SPEED)
            if speed > 0:
                left_update = running_time()
                
        elif wheel == 'R':
            right_speed = amap(speed, 0, 100, 0, MAX_SPEED)
            if speed > 0:
                right_update = running_time()    
        print(left_speed, right_speed)
    if running_time() - left_update > DELAY:
        left_speed = -0.2
        print(left_speed, right_speed)
    if running_time() - right_update > DELAY:
        right_speed = -0.2
        print(left_speed, right_speed)
    
    # Update display
    if running_time() - led_update > 50:
        
        
        if left_speed < 0 and right_speed < 0:
            led_update = running_time()
            display.show(Image.ARROW_S)
            continue
        if left_speed < 0:
            index = 0
        elif right_speed < 0:
            index = -1
        else:
            index = int(amap(left_speed - right_speed, -1, 1, 0, len(led_edges)))
            
        last_points.append(led_edges[index])
        last_points.pop(0)
        
        for i, point in enumerate(last_points):
            x, y = point
            draw_line(Vector(2, 3), Vector(x, y), [1, 3, 5, 7, 9][5-len(last_points) + i])
            
        for y, row in enumerate(led_array):
            for x, bright in enumerate(row):
                display.set_pixel(x, y, bright)
                led_array[y][x] = 0
        
        led_update = running_time()
    