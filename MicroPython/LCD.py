from machine import Pin, I2C, SoftI2C
from esp8266_i2c_lcd import I2cLcd
from time import sleep

DEFAULT_I2C_ADDR = 0x27
hw_i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=200000)
lcd = I2cLcd(hw_i2c, DEFAULT_I2C_ADDR, 4, 20)
lcd.putstr("Hello World ~~")
while 1:
    pass