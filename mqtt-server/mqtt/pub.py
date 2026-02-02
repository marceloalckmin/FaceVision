from paho.mqtt import client as mqtt
import json

client = mqtt.Client()
client.connect("localhost", 1883)

msg = {
    "nome": "Marcelo Alckmin",
    "matricula": "119",
    "sala": "I-22",
    "materia": "C210 - Inteligência Computacional"
}

client.publish("facevision/presenca", json.dumps(msg))
print("Mensagem enviada")