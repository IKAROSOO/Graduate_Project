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

client.connect("test.mosquitto.org", 1883, 60)

#mqtt.eclipse.org는 더 이상 사용불가
#test.mosquitto.org로 변경

client.loop_forever()