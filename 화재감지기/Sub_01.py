import paho.mqtt.client as mqtt

server = 'test.mosquitto.org'

topic_Fireflag = "id/Fire_flag/on"

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code : " + str(rc))
    client.subscribe(topic_Fireflag)

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode('utf-8'))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server)

client.loop_forever()