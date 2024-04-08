import paho.mqtt.client as mqtt

server = 'test.mosquitto.org'

topic_Fireflag = "id/Fire_flag/on"

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code" + str(rc))
    client.subscribe(topic_Fireflag)

def on_message(client, userdata, msg):
    Fireflag = msg.payload.decode('utf-8')
    #On 일 경우 소화기가 들어진 것
    #Off 일 경우 소화기가 놓아진 것

    if Fireflag == "on":
        print("Fire flag is on")
    else:
        print("Fire flag is off")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(server)

client.loop_forever()
