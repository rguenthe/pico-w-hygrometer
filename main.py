import time
import machine
import dht

import wifi
from secrets import WIFI_SSID, WIFI_PASSWORD, THINGSPEAK_WRITE_API_KEY


THINGSPEAK_URL = "https://api.thingspeak.com/update"
DHT_DATA_PIN = 28
LED_PIN = "LED" # internal LED

# init LED
led_pin = machine.Pin(LED_PIN, machine.Pin.OUT)

# init DHT22 sensor
dht_sensor = dht.DHT22(machine.Pin(DHT_DATA_PIN))

# connect wifi
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while True:
    # heartbeat
    led_pin.toggle()

    # read sensor
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    
    # upload values
    data = {
        "api_key": THINGSPEAK_WRITE_API_KEY,
        "field1": temperature,
        "field2": humidity
    }
    wifi.upload_data(THINGSPEAK_URL, data)
    time.sleep(10)
