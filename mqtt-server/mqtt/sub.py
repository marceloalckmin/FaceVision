from paho.mqtt import client as mqtt

def on_message(client, userdata, msg):
    print("Recebido:", msg.payload.decode())

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("facevision/presenca")
client.on_message = on_message

client.loop_forever()
