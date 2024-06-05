from machine import Pin
import time

led= Pin(25,Pin.OUT)

while 1:
    led.on()
    time.sleep_ms(1000)
    led.off()
    time.sleep_ms(1000)