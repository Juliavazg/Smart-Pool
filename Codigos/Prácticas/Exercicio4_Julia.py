from machine import ADC, Pin, PWM
import random
from time import sleep_ms

pot = ADC(26)
rojo = PWM(Pin(15))
azul = PWM(Pin(14))
verde = PWM(Pin(16))
pulsador = Pin(20,Pin.IN,Pin.PULL_DOWN)

n = 0

while True:
   if pulsador.value() == 1:
      n += 1
if n == 1:
   brilloazarR = random.randint(0,65535)
   brilloazarB = random.randint(0,65535)
   brilloazarG = random.randint(0,65535)
   rojo.duty_u16(brilloazarR)
   azul.duty_u16(brilloazarB)
   verde.duty_u16(brilloazarG)
if n>1:
   n = 0 