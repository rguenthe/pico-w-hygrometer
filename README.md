# Raspberry Pi Pico W Hygrometer (Micropython)

Wifi-connected thermometer and hygrometer. Uses the DHT22 sensor and uploads data to thingspeak.com.

## Operation

Measurement/Upload is done every 5 minutes. If no wifi is available the measured data will be lost. 
During the measurment the internal LED is on, inbetween measurement the LED pulses at ~1 Hz to signal a sign of life.

## Usage

A file `secrets.py` must be created containing wifi network information (ssids/passwords) and API keys for the data upload.


### Example for secrets.py
```python
WIFI_KNOWN_NETWORKS = [
    {
        "ssid":">>>first-network-ssid<<<",
        "password":">>>first-network-password<<<"
    },
    {
        "ssid":">>>second-network-ssid<<<",
        "password":">>>second-network-password<<<"
    }
]

UPLOAD_WRITE_API_KEY = ">>>your-api-key<<<"
UPLOAD_READ_API_KEY =  ">>>your-api-key<<<"
```