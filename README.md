# IoT-ESP32
Use ESP32 to build an air quality detect system.

# Version
* ![Micropython v1.14]()

# Micropython/
* main.py: Code for a system to use CO2, PM2.5, Temperature, Humidity and LCD Screen.
* CCS811.py: Code for CO2 Sensor.
* DHT22.py: Code for Temperature and Humidity Sensor.
* GP2Y.py: Code for PM2.5 Sensor.
* LCD.py: Code for LCD Screen.
* OLED.py: Code for OLED Screen.

* libraies for codes above:
    * lcd_api.py: LCD libraries.
    * esp8266_i2c_lcd.py: LCD libraries based on lcd_api.
    * ssd1306.py: OLED libraries.

# Ref
* ![DHT22]()
* ![CCS811]()
* ![GP2Y]()
* ![LCD]()
* ![OLED]