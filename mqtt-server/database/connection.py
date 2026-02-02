import json
import mysql.connector
from paho.mqtt import client as mqtt

db = mysql.connector.connect(user = 'facevision', password = 'facevision', host = 'localhost', database = 'Frequencia_Inatel')

cursor = db.cursor()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    cursor.execute(
        "INSERT INTO presenca (nome, matricula, sala, materia, data_hora) VALUES (%s, %s, %s, %s, NOW())",
        (data["nome"], data['matricula'], data['sala'], data.get("materia", "N/A"))
    )

    db.commit()

    print("Presenca salva: ", data['nome'])

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("facevision/presenca")
client.on_message = on_message

print("MQTT + DB rodando!")
client.loop_forever()
