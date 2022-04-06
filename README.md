# IoT-ESP32
Use ESP32 to build an air quality detect system.
<img src="https://github.com/Ratherman/IoT-ESP32/blob/main/Pic/Demo.jpeg" width=30%>

# ESP32 Spec
<img src="https://github.com/Ratherman/IoT-ESP32/blob/main/Pic/ESP32-SPEC.jpeg" width=400>

# Environment
* [Micropython v1.14](https://docs.micropython.org/en/v1.14/library/index.html)
    * Download binary [here](https://micropython.org/download/esp32/)
    * <img src="https://github.com/Ratherman/IoT-ESP32/blob/main/Pic/Micropython_binary.jpg" width=400>


* [Thonny IDE](https://thonny.org/)
* [CP210x driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
* WIN 11

# Micropython/
* `main.py`: Code for a system to use CO2, PM2.5, Temperature, Humidity and LCD Screen.
* `CCS811.py`: Code for CO2 Sensor.
* `DHT22.py`: Code for Temperature and Humidity Sensor.
* `GP2Y.py`: Code for PM2.5 Sensor.
* `LCD.py`: Code for LCD Screen.
* `OLED.py`: Code for OLED Screen.

* Libraies for codes above:
    * `lcd_api.py`: LCD libraries.
    * `esp8266_i2c_lcd.py`: LCD libraries based on lcd_api.
    * `ssd1306.py`: OLED libraries.

# Ref
* [DHT22](https://randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor/)
* [CCS811](https://github.com/Notthemarsian/CCS811)
* [GP2Y](https://rntlab.com/question/esp32-read-sharp-dust-sensor-gp2y10-switch-micropython/)
    * Note: Changes are needed to make LED work, please check `main.py` or `GP2Y.py` for details.
* [LCD](https://microcontrollerslab.com/i2c-lcd-esp32-esp8266-micropython-tutorial/)
* [OLED](https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/)