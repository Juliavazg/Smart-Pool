from machine import Pin, PWM
import time

motor_1A = PWM(Pin(8))
motor_1B = PWM(Pin(9))
pulsador = Pin(20,Pin.IN,Pin.PULL_UP)
pulsador2 = Pin(21,Pin.IN,Pin.PULL_UP)

motor_1A.freq(10000)
motor_1B.freq(10000)
n=0

while True:
    if pulsador.value() == 1:
        n
        motor_1A.duty_u16(0) 
        motor_1B.duty_u16(0)
        time.sleep_ms(200)
    if pulsador.value() == 1:
        n =n+1
        motor_1A.duty_u16(55000) 
        motor_1B.duty_u16(0)
        time.sleep_ms(200)
    if pulsador.value() == 1:
        n =n+2
        motor_1A.duty_u16(0) 
        motor_1B.duty_u16(55000)
        time.sleep_ms(200)
    if pulsador2.value() == 1:
        motor_1A.duty_u16(0) 
        motor_1B.duty_u16(0)
    