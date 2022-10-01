import network
import time
import urequests
import json


def connect(ssid, password):
    """
    connect to wifi network
    """
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    if not wifi.isconnected():
        print("connect to wifi '{}'".format(ssid))
        wifi.connect(ssid, password)

        print("waiting for WIFI connection...")
        wait_connection = 10
        while not wifi.isconnected() and wait_connection > 0:
            time.sleep(1)
            wait_connection -= 1

        if wifi.isconnected():
            print("connected")
            ret = True
        else:
            print("connection failed")
            ret = False
    else:
        print("wifi '{}' already connected".format(ssid))
        ret = True

    return ret


def upload_data(url, payload=None):
    """
    upload data using HTTP POST request with JSON payload
    """
    print("uploading data to '{}'".format(url))
    success = False
    retries = 3

    headers = {'Content-Type':'application/json'}
    data = (json.dumps(payload)).encode()

    while not success and retries > 0:
        response = urequests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            success = True
            print("upload successful")
        else:
            retries -= 1
            print("upload failed with code {}. Try again...".format(response.status_code))
        response.close()
