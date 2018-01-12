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

move_toggle = 0
radio.on()
radio.config(channel=71, group=16)

while True:
    radio_msg = radio.receive()
    if radio_msg and radio_msg.startswith("bit:bot_activate"):
        
    if move_toggle and radio_forward:
        
    else:
        robot_move(0, 0, 0)
    
    if button_a.was_pressed():
        move_toggle = not move_toggle