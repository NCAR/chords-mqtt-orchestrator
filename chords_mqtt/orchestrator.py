#!/usr/bin/env python
import paho.mqtt.client as mqtt
import requests
import yaml

from .config import config as cfg

# todo : add logging


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for topic in cfg['mqtt']['topics']:
        client.subscribe(topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    instruments = cfg['chords']['instruments']
    email = cfg['chords']['email']
    api_key = cfg['chords']['api_key']

    try:
        data = yaml.load(msg.payload, Loader=yaml.FullLoader)
        sensor, measurement = data['instrument'].split('/')

        if sensor in instruments.keys():
            var = instruments[sensor].get(measurement, False)

        sensor_id = data['device'].split('/')[1]
        parameters = 'sensor_id={}&{}={}&email={}&api_key={}&test'.format(
            sensor_id, var, data['m'], email, api_key
        )

        r = requests.get(
            '{}/measurements/url_create?{}'.format(cfg['chords']['base_api_endpoint'], parameters)
        )

        if r.status_code == 200:
            print(
                '[info]: data successfully sent to chords at {}'.format(
                    cfg['chords']['base_api_endpoint']
                )
            )
        else:
            print('[warn]: {} - {}'.format(r.status_code, r.content))
    except Exception as e:
        print('[error]: {}'.format(e))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(cfg['mqtt']['host'], cfg['mqtt']['port'], 60)
    client.loop_forever()

    # todo : add testing
