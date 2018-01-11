def amap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

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
    def __init__(self, robot):
        self.robot = robot
        self.left_speed = 0
        self.right_speed = 0

    def update(self):
        msg = radio.receive()
        if msg:
            wheel, speed = msg.split()
            if wheel == 'L':
                self.left_speed = amap(speed, -100, 100, -Controller.MAX_SPEED, Controller.MAX_SPEED)
            elif wheel == 'R':
                self.right_speed = amap(speed, -100, 100, -Controller.MAX_SPEED, Controller.MAX_SPEED)
        self.robot.motors(self.left_speed, self.right_speed)

