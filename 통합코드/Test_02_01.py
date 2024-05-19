from gtts import gTTS
import threading
import paho.mqtt.client as mqtt
import time

TOPICS =[("topic/locate", 0), ("topic/flag", 0)]

global msg_in_flag
msg_in_flag = False

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code" + str(rc))
    
    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global msg_in_flag

    topic = msg.topic
    message = msg.payload.decode()

    if topic == "topic/locate":
        print(message)
        return message

def mqtt_thread():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connectt("test.mosquitto.org", 1883, 60)

    client.loop_forever()

    time.sleep(0.1)

def TTS_thread(text):
    tts = gTTS(text=text, lang='ko')
    tts.save(TTS.mp3)

text = "현재 불이 난 곳은 {}".format()

thread_Mqtt = threading.Thread(target= mqtt_thread)
thread_TTS = threading.Thread(target= TTS_thread, args= ())