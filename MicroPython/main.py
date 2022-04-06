from machine import I2C, Pin, SoftI2C, ADC
from esp8266_i2c_lcd import I2cLcd
from CCS811 import CCS811
from time import sleep
import dht
from utime import sleep, sleep_us

# PM2.5
PM25_Sensor = ADC(Pin(32))
PM25_Sensor.atten(ADC.ATTN_11DB) #range 0-4095 -> 3,3 V
PM25_LedPower = Pin(16, Pin.OUT)
_samplingTime = 280 #original 280
_deltaTime = 40
_sleepTime = 9680

# Temperature and Humidity
TEMP_Sensor=dht.DHT22(Pin(14))

# CO2
CO2_i2c = SoftI2C(scl=Pin(26), sda=Pin(27))
CO2_Sensor = CCS811(CO2_i2c)

# LCD
DEFAULT_I2C_ADDR = 0x27
LCD_i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=200000)
LCD_Screen = I2cLcd(LCD_i2c, DEFAULT_I2C_ADDR, 4, 20)

while True:
    #=======#
    # PM2.5 #
    #=======#
    PM25_LedPower.off()
    sleep_us(_samplingTime)
    voMeasured = PM25_Sensor.read() # read Dust Value
    sleep_us(_deltaTime)
    PM25_LedPower.on()
    sleep_us(_sleepTime)
    calcVoltage = voMeasured * (5 / 4096)    #0 – 5 V mapped to 0 – 4095
    PM25 = 170 * calcVoltage - 0.01
    
    # ====================== #
    # Humidity & Temperature #
    # ====================== #
    TEMP_Sensor.measure()
    TEMP=TEMP_Sensor.temperature()
    HUMI=TEMP_Sensor.humidity()
    
    #=====#
    # CO2 #
    #=====#
    CO2 = 0
    if CO2_Sensor.data_ready():
        CO2 = CO2_Sensor.eCO2
    
    LCD_Screen.clear()
    
    # 第一行
    LCD_Screen.move_to(0,0)
    LCD_Screen.putstr("Temperature: ")
    LCD_Screen.move_to(14,0)
    LCD_Screen.putstr("{0:3.1f} C\n".format(TEMP))
    
    # 第二行
    LCD_Screen.putstr("Humidity: ")
    LCD_Screen.move_to(14,1)
    LCD_Screen.putstr("{0:3.1f} %\n".format(HUMI))

    # 第三行
    LCD_Screen.putstr("PM 2.5: ")
    if PM25 > 100:
        LCD_Screen.move_to(9,2)
    else: # PM25 < 100
        LCD_Screen.move_to(10,2)
    LCD_Screen.putstr("{0:3.1f} ug/m3\n".format(PM25))
    
    # 第四行
    LCD_Screen.putstr("CO2: ")
    if CO2 < 1000:
        LCD_Screen.move_to(13, 3)
    else: # CO2 < 1000
        LCD_Screen.move_to(12, 3)
    LCD_Screen.putstr("{:d} ppm".format(CO2))
    sleep(5)
    
