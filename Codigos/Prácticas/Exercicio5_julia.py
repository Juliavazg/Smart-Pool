from machine import Pin, PWM
import time

motor_1A = PWM(Pin(8))
motor_1B = PWM(Pin(9))
pulsador = Pin(20,Pin.IN,Pin.PULL_UP)
vel=20000

motor_1A.freq(10000)
motor_1B.freq(10000)

while True:
    if pulsador.value() == 1:
        vel=vel+5000
        time.sleep_ms(200)
        
    if  vel>65535:
        vel=20000
        
    motor_1A.duty_u16(vel) 
    motor_1B.duty_u16(0)