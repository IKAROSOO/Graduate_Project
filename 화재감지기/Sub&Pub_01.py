import paho.mqtt.client as mqtt

topic = 'id/Fire_Detect'

server = 'test.mosquitto.org'

def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    data = eval(msg.payload.decode())

    if str(data[1]) == 'on':
        print("현재 화재가 난 곳은 {}호입니다.".format(data[0]))
        client.publish("id/Fire_flag/on", "on")
    else:
        print("현재 화재가 발생하지 않았습니다.")
        client.publish("id/Fire_flag/on", "off")
    

client = mqtt.Client()
client.connect(server, 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

