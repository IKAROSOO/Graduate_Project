import paho.mqtt.client as mqtt

#On일 경우, 소화기가 들려진 경우
#Off일 경우, 소화기가 놓아진 경우

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code" + str(rc))

    client.subscribe("topic/on")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()