import sys
import paho.mqtt.client as mqtt

topic = "id/room_num/"
#server = "iotlab101.io7lab.com"
server = "test.mosquitto.org"
def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    measurement = eval(msg.payload.decode())
    print(measurement)
    print(type(measurement[0]))
#list 0번은 int형
#list 1번은 str형

client = mqtt.Client()
client.connect(server, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()