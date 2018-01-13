from microbit import *
import radio

def robot_move(r_value, l_value, slp_time):
    pin1.write_analog(r_value)
    pin12.write_digital(0)
    pin0.write_analog(l_value)
    pin8.write_digital(0)
    sleep(slp_time)
    pin1.write_digital(0)
    pin12.write_digital(0)
    pin0.write_digital(0)
    pin8.write_digital(0)

def radio_move(direct):
    if direct == 'forwards':
        for i in range(move_for_steps):
            if light_sens_val_1 and light_sens_val_2:
                robot_move(1023, 1023, 100)
    elif direct == 'left':
        robot_move(1023, 0, 235)
    elif direct == 'right':
        robot_move(0, 1023, 235)

move_commands = ['forwards', 'left', 'right']
radio.on()
radio.config(channel=71)
move_for_steps = 10

while True:
    light_sens_val_1 = pin11.read_digital()
    light_sens_val_2 = pin5.read_digital()
    
    radio_msg = radio.receive()
    
    if radio_msg and radio_msg.startswith("INPT_BTBT-"):
        msg_command = radio_msg.split('-')[1]
        if msg_command in move_commands:
            radio_move(msg_command)