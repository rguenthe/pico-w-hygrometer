import network
import time
import urequests
import json


def connect(ssid, password):

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    if not wifi.isconnected():
        wifi.connect(ssid, password)
        print("Waiting for connection...")

        while not wifi.isconnected():
            time.sleep(1)
        print("connected")

    else:
        print("Already connected")


def upload_data(url, payload=None):
    
    success = False
    retries = 3

    headers = {'Content-Type':'application/json'}
    data = (json.dumps(payload)).encode()
    
    while not success and retries > 0:
        response = urequests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            success = True
        else:
            retries -= 1
