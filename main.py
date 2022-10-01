import time
import machine
import dht
import wifi

from secrets import WIFI_KNOWN_NETWORKS, UPLOAD_WRITE_API_KEY


UPLOAD_URL = "https://api.thingspeak.com/update"
DHT_DATA_PIN = 28
LED_PIN = "LED" # internal LED
MEASUREMENT_CYCLE = 300


def dht_measure_and_upload(dht_sensor):
    """
    perform DHT measurement and upload data
    """
    print("read sensor")
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    print("check wifi connection")
    if wifi.connect(WIFI_KNOWN_NETWORKS) == True:

        print("upload data")
        data = {
            "api_key": UPLOAD_WRITE_API_KEY,
            "field1": temperature,
            "field2": humidity
        }
        wifi.upload_data(UPLOAD_URL, data)


#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------

# init LED
led_pin = machine.Pin(LED_PIN, machine.Pin.OUT)

# init DHT22 sensor
dht_sensor = dht.DHT22(machine.Pin(DHT_DATA_PIN))

# measurement scheduling
measurement_timer = MEASUREMENT_CYCLE
measurment_scheduled = True

while True:
    # heartbeat
    led_pin.off()
    time.sleep(0.9)
    led_pin.on()
    time.sleep(0.1)

    # update measurement timer
    measurement_timer -= 1
    if measurement_timer == 0:
        measurment_scheduled = True

    if measurment_scheduled:
        # perform scheduled measurement
        dht_measure_and_upload(dht_sensor)

        print("next measurment in {} seconds".format(MEASUREMENT_CYCLE))
        measurement_timer = MEASUREMENT_CYCLE
        measurment_scheduled = False
