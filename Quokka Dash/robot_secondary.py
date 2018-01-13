from microbit import *
import radio

left_speed = 0
right_speed = 0

led_update = 0

sc = 62
gc = 72

MAX_SPEED = 0.6
DELAY = 1000

led_edges = [(0, 3), (0, 2), (1, 1), (2, 1), (3, 1), (4, 2), (4, 3)]
all_edges = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4), (4, 3), (4, 2), (4, 1), (3, 0), (2, 0), (1, 0)]
led_array = [[0 for x in range(5)] for y in range(5)]
last_points = [(2, 1)]

current = 0

radio.on()

def amap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        
def draw_line(start, end, b=9):
    if start[0] == end[0]:
        for y in range(start[1], end[1] + [-1, 1][end[1] > start[1]], [-1, 1][start[1] < end[1]]):
            led_array[y][start[0]] = b
        return
    if start[0] > end[0]:
        start, end = end, start
    m = (start[1] - end[1]) / (start[0] - end[0])
    c = start[1] - m * start[0]
    l = int(((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5) + 1 
    for gap in range(l + 1):
        x = amap(gap, 0, l, start[0], end[0])
        y = m * x + c
        led_array[min(max(int(y + 0.5), 0), 4)][min(max(int(x + 0.5), 0), 4)] = b
    
while True:
    
    radio.config(channel=sc)
    
    while True:
        msg = radio.receive()
        if msg == 'start':
            radio.config(channel=gc)
            break
        last_points.append(all_edges[current])
        current = (current - 1) % len(all_edges)
        while len(last_points) > 5:
            last_points.pop(0)
        for i in range(len(last_points)):
            x, y = last_points[i]
            draw_line((2, 2), (x, y), [1, 3, 5, 7, 9][5-len(last_points) + i])
        for y, row in enumerate(led_array):
            for x, bright in enumerate(row):
                display.set_pixel(x, y, bright)
                led_array[y][x] = 0
            led_array = [[0 for x in range(5)] for y in range(5)]    
    radio.on()
    for i in range(5):
        display.show(Image((str(1+i*2)*5+':')*5))
        sleep(100)
    display.clear()
    left_update = running_time()
    right_update = running_time()
    while True:
        msg = radio.receive()
        if msg:
            if msg == 'stop':
                break
            try:
                wheel, speed = msg.split(':')
            except:
                continue
            speed = int(speed)
            if wheel == 'L':
                left_speed = amap(speed, 0, 100, 0, MAX_SPEED)
                if speed > 0:
                    left_update = running_time()
            elif wheel == 'R':
                right_speed = amap(speed, 0, 100, 0, MAX_SPEED)
                if speed > 0:
                    right_update = running_time() 
        if running_time() - left_update > DELAY:
            left_speed = -0.2
        if running_time() - right_update > DELAY:
            right_speed = -0.2
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
                draw_line((2, 3), (x, y), [1, 3, 5, 7, 9][5-len(last_points) + i])
            for y, row in enumerate(led_array):
                for x, bright in enumerate(row):
                    display.set_pixel(x, y, bright)
                    led_array[y][x] = 0
            led_update = running_time()
        