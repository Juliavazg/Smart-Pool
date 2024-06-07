import dht
from machine import I2C, Pin, ADC, PWM
import time 
from esp8266_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0X27
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

sdaPIN = machine.Pin(0)
sclPIN = machine.Pin(1)
d = dht.DHT11(machine.Pin(12))
rele=Pin(7,Pin.OUT)

ldr= ADC(26)
luz = ldr.read_u16()

global temp
global hum
    
while True:
    
    time.sleep(2)
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(temp)
    time.sleep(1)
    print(hum)
    time.sleep(1)
    
    if temp>10:
        rele.off()
    else:
        rele.on()
        
    
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Julia")
    lcd.move_to(0, 1)
    lcd.putstr("Vazquez Gonzalez")
    time.sleep(1)
    
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Smart Pool")
    lcd.move_to(0, 1)
    lcd.putstr("IES de Teis")
    time.sleep(3)

    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Temperatura: "+ str(temp) + chr (0xDF) + "C")
    lcd.move_to(0, 1)
    lcd.putstr("Humidade: " + str(hum) + "%")
    time.sleep(3)
    
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Luz:")
    lcd.move_to(6, 0)
    lcd.putstr(str(luz))
    time.sleep(3)
    
