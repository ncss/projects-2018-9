from microbit import *
display.off()
while True:
    pin3.write_digital(1)
    pin2.write_digital(1)
    pin1.write_digital(1)
    pin0.write_digital(1)
    sleep(500)
    pin3.write_digital(0)
    pin2.write_digital(0)
    pin1.write_digital(0)
    pin0.write_digital(0)
    sleep(500  )
