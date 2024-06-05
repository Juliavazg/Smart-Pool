from machine import Pin, PWM
import time

servo= PWM(Pin(15))
servo.freq(50)
pulsador = Pin(20,Pin.IN,Pin.PULL_UP)
n=0

while True:
    if pulsador.value() == 1:
       n=n+1
    if n>2:
       n=0
    if n==0:
         servo.duty_ns(500000)
         time.sleep_ms(100)
    elif n==1:
         servo.duty_ns(1500000)
         time.sleep_ms(100)
    elif n==2:
         servo.duty_ns(2500000)
         time.sleep_ms(100)
    else:
         servo.duty_ns(500000)