# IoT-ESP32
Use ESP32 to build an air quality detect system.

* Step 1: Download [Arduino IDE](https://www.arduino.cc/en/software)
* Step 2: Install ESP32 in Arduino IDE
    1. 設定 package 路徑 URL
        * 開啟 Arduino > 檔案 > 偏好設定
        * 於額外的開發板管理員網址填入:`https://dl.espressif.com/dl/package_esp32_index.json`
    2. 安裝 ESP32 開發板
        * 開啟 Arduino > 工具 > 開發板 > 開發板管理員
        * 搜尋 ESP32 > 安裝
        * Note: 安裝時間 2022/03/27 版本為 1.0.6
    3. 設定 ESP32 開發板
        * 工具 > 開發板 > 開發板廠商(i.e., NodeMCU-32S)

* Step 3: ESP32 + DHT22
    * 工具 > 管理程式庫 > 搜尋**DHT22**

# Reference
* Step 2 Ref. : https://www.youtube.com/watch?v=wC_I8BKsOr0