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
                for i in range(3):
                    radio.send("INPT_BTBT-forwards")
                    sleep(50)
                #print("forward")
            elif count > num:
                for i in range(3):
                    radio.send("INPT_BTBT-right")
                    sleep(50)
                #print("right")
            elif count < num:
                for i in range(3): 
                    radio.send("INPT_BTBT-left")
                    sleep(50)
                #print("left")
            for i in range(3):
                radio.send("INPT_RNDM-1")
                sleep(50)
            #print("done")
            display.scroll("SENT")
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