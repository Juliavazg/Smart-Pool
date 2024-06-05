from machine import Pin, PWM
import time

servo= PinPWM(Pin(15))
servo.freq(50)
pulsador = Pin(20,Pin.IN,Pin.PULL_UP)

n=0

while True:
    if pulsador.value() == 0 and prev_pulsador == 1:
    else n+=1
    if n>2 n=0
    if n=0
    else servo=0
    if n=1
    else servo=90
    in n=2
    else servo=180
        
        