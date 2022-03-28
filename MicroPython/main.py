#from bmp180 import BMP180
from machine import I2C, Pin, SoftI2C, ADC
from esp8266_i2c_lcd import I2cLcd
from time import sleep
import dht
from utime import sleep, sleep_us
measurePIN = ADC(Pin(32))
#measurePIN = Pin(32)
measurePIN.atten(ADC.ATTN_11DB) #range 0-4095 -> 3,3 V
LedPower = Pin(16, Pin.OUT)
samplingTime = 280 #original 280
deltaTime = 40
sleepTime = 9680
voMeasured = 0
calcVoltage = 0
dustDensity = 0

sensor=dht.DHT22(Pin(14))

# i2c = SoftI2C(scl=Pin(26), sda=Pin(27))
# p = BMP180(i2c)
DEFAULT_I2C_ADDR = 0x27
hw_i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=200000)
lcd = I2cLcd(hw_i2c, DEFAULT_I2C_ADDR, 4, 20)

while True:
    #print("temperature:", p.temperature, "Air pressure:", p.pressure/100, "altitude:", p.altitude)
    LedPower.off()
    sleep_us(samplingTime)
    voMeasured = measurePIN.read() # read Dust Value
    sleep_us(deltaTime)
    LedPower.on()
    sleep_us(sleepTime)

    #0 – 5 V mapped to 0 – 4095
    calcVoltage = voMeasured * (5 / 4096)
    dustDensity = 170 * calcVoltage - 0.01
    
    sensor.measure()
    temp=sensor.temperature()
    hum=sensor.humidity()
    lcd.clear()
    lcd.move_to(0,0)
    #lcd.putstr(str(p.temperature)+" C\n")
    lcd.putstr("Temperature: ")
    lcd.move_to(14,0)
    lcd.putstr("{0:3.1f} C\n".format(temp))
    lcd.putstr("Humidity: ")
    lcd.move_to(14,1)
    lcd.putstr("{0:3.1f} %\n".format(hum))
    lcd.putstr("PM 2.5: ")
    lcd.move_to(10,2)
    lcd.putstr("{0:3.1f} ug/m3\n".format(dustDensity))
    #lcd.move_to(17,3)
    #lcd.putstr("hPa")
    sleep(2)
    
