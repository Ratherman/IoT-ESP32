from machine import Pin, ADC
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

print("***************** START *************************")
while True:
    LedPower.off()
    sleep_us(samplingTime)
    voMeasured = measurePIN.read() # read Dust Value
    sleep_us(deltaTime)
    LedPower.on()
    sleep_us(sleepTime)

    #0 – 5 V mapped to 0 – 4095
    calcVoltage = voMeasured * (5 / 4096)
    dustDensity = 170 * calcVoltage - 0.01

    print("Raw Signal Value (0-4095): {0:3.2f}".format(voMeasured))
    print(" – Voltage: {0:3.2f}".format(calcVoltage))
    print(" – Dust Density: {0:3.2f} ug/m3".format(dustDensity))

    sleep(1)

    print("***************** ENDE *************************")
