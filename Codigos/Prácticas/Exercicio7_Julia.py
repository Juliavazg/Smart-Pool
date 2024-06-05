from machine import ADC, Pin, PWM
import time

ldr= ADC(27)
motor_1A = PWM(Pin(8))
motor_1B = PWM(Pin(9))

motor_1A.freq(10000)
motor_1B.freq(10000)

while True:
    luz = ldr.read_u16()
    print ("Luz: " + str(luz))
    if luz > 32500:
        motor_1A.duty_u16(luz) 
        motor_1B.duty_u16(0)
    else:
        motor_1A.duty_u16(0) 
        motor_1B.duty_u16(0)
    time.sleep_ms(100)      