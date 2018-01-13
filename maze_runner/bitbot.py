from microbit import *
import radio

move_commands = ['forwards', 'left', 'right']

radio.on()
radio.config(channel=71)
move_val = 1023

def robot_move(r_value, l_value):
    # right motor
    pin12.write_digital(0)
    pin1.write_analog(r_value)
    
    # left motor
    pin8.write_digital(0)
    pin0.write_analog(l_value)
    
def robot_stop():
    pin12.write_digital(0)
    pin1.write_analog(0)
    pin8.write_digital(0)
    pin0.write_analog(0)

def radio_move(direct):
    if direct == 'forwards':
        robot_move((move_val >> 1) + 150, (move_val >> 1))
    elif direct == 'left':
        #robot_move(move_val, 0, 235)
        robot_move(move_val, 0)
    elif direct == 'right':
        #robot_move(0, move_val, 235)
        robot_move(0, move_val)
    
    MOVE_TIME = 1000
    stop_time = running_time() + MOVE_TIME
    
    while (running_time() <= stop_time) and (pin11.read_digital() or pin5.read_digital()):
        continue
    robot_stop()
    
while True:
    radio_msg = radio.receive()
    if radio_msg and radio_msg.startswith("INPT_BTBT-"):
        msg_command = radio_msg.split('-')[1]
        #if msg_command in move_commands:
        #    radio_move(msg_command)
        radio_move(radio_msg[10:])
