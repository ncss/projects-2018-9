from microbit import *
import radio

def robot_move(r_value, l_value, slp_time):
    pin0.write_analog(r_value)
    pin16.write_digital(0)
    pin8.write_analog(l_value)
    pin12.write_digital(0)
    sleep(slp_time)
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)
    
def radio_move(direct):
    if move_toggle:
        if direct == 'forwards':
            for i in range(20):
                if light_sens_val_1 and light_sens_val_2:
                    robot_move(1023, 1023, 50)
        elif direct == 'left':
            robot_move(1023, 0, 230)
        elif direct == 'right':
            robot_move(0, 1023, 230)

move_commands = ['forwards', 'left', 'right']
move_toggle = 0
radio.on()
radio.config(channel=66)

while True:
    radio_msg = radio.receive()
    display.clear()
    if radio_msg and radio_msg.startswith("INPT_BTBT-"):
        display.show(Image.HAPPY)
        msg_command = radio_msg.split('-')[1]
        if msg_command in move_commands:
            radio_move(msg_command)
    
    if button_a.was_pressed():
        move_toggle = not move_toggle