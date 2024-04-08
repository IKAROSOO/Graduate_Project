import sys
import paho.mqtt.client as mqtt

server = 'test.mosquitto.org'

client = mqtt.Client()
client.connect(server, 1883, 60)

if len(sys.argv) <= 1:
    print("Usage : " + sys.argv[0] + "messasge")
    exit()
else:
    client.publish("id/Fire_flag/on", str(sys.argv[1]))