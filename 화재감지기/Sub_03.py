import paho.mqtt.client as mqtt

server = 'test.mosquitto.org'

topic_Fireflag = "id/Fire_flag/on"

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code" + str(rc))
    client.subscribe(topic_Fireflag)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    data = msg.split(":")

    for i in len(data):
        print(data[i])


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server, 1883, 60)

client.loop_forever()