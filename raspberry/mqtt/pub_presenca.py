from paho.mqtt import client as mqtt
import json

def pub_presenca(data):
    client = mqtt.Client()
    client.connect("192.168.0.106", 1883)

    client.publish(
        "facevision/presenca",
        json.dumps(data)
    )

    client.disconnect()
