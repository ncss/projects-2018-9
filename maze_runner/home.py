from microbit import *
import radio

#currently_held = False
previously_held = False    
def pin_was_pressed(pinX, previously_held):#, currently_held):
    #currently_held = False
    #previously_held = False
    wp = False
    currently_held = pinX.read_digital()
    
    if (previously_held != currently_held) and (currently_held == True):
        wp = True
    else:
        wp = False
    
    previously_held = currently_held
    return (wp, previously_held)#, currently_held)

num = 0
count = 0
radio.on()
radio.config(channel=71)
while True:
    if num:
        display.show(str(count))
        p = pin_was_pressed(pin0, previously_held)#, currently_held)
        previously_held = p[1]
        #currently_held = p[2]
        if p[0]:
            if count == num:
                radio.send("INPT_BTBT-forwards")
                print("forward")
            elif count > num:
                radio.send("INPT_BTBT-right")
                print("right")
            elif count < num:
                radio.send("INPT_BTBT-left")
                print("left")
                
            sleep(50)
            radio.send("INPT_RNDM-1")
            print("done")
            num = 0
            count = 0
        elif button_b.was_pressed():
            count = (count + 1) % 10
        elif button_a.was_pressed():
            count = (count + 9) % 10
    else:
        display.show(Image.SAD)
        msg = radio.receive()
        if msg and msg.startswith("RNDM_INPT-"):
            print(msg)
            num = int(msg[10])
            