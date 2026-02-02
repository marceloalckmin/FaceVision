from paho.mqtt import client as mqtt
import json

def publish_presence(data):
    client = mqtt.Client()
    client.connect("IP_DO_SERVIDOR", 1883)

    client.publish(
        "facevision/presenca",
        json.dumps(data)
    )

    client.disconnect()
