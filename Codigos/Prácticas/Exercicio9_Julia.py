from machine import I2C, Pin, dht
from esp8266_i2c_lcd import I2cLcd
from time import sleep_ms

sdaPIN = machine.Pin(0)
sclPIN = machine.Pin(1)

DEFAULT_I2C_ADDR = 0X27
i2c = machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

global temp
global hum

d = dht.DHT11(machine.Pin(12))

while True:

    time.sleep(2)
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(f"Temperatura: {temp}ºC")
    print(f"Humedad: {hum}%")

    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(f"Temperatura: {temp} ºC")
    lcd.move_to(0, 1)
    lcd.putstr(f"Humedad: {hum}%")