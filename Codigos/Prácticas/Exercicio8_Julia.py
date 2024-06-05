from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0X27
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

    
while True:
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Julia")
    lcd.move_to(0, 1)
    lcd.putstr("Vázquez González")
    sleep_ms(3000)

    lcd.clear()

    lcd.move_to(0, 0)
    lcd.putstr("smart pool")
    lcd.move_to(0, 1)
    lcd.putstr("IES de Teis")
    sleep_ms(3000)