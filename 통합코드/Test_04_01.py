from gtts import gTTS
import paho.mqtt.client as mqtt
import threading
import time

TOPICS = [("topic/tts", 0)]
server = "test.mosquitto.org"
savepoint = "./통합코드/TTS_04_01.mp3"
locate = None

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code " + str(rc))

    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global locate
    locate = msg.payload.decode()

    # TTS 처리 스레드를 메시지를 받을 때마다 실행합니다.
    thread_TTS = threading.Thread(target=TTS_thread, args=(locate, savepoint))
    thread_TTS.start()

def mqtt_thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, 1883, 60)
    client.loop_forever()

def TTS_thread(locate, savepoint):
    if locate:
        text = "현재 화재가 발생한 곳은 " + locate + "호 입니다."
        tts = gTTS(text=text, lang='ko')
        tts.save(savepoint)
        print(f"TTS 저장 완료: {savepoint}")

# MQTT 스레드를 시작합니다.
thread_Mqtt = threading.Thread(target=mqtt_thread, args=(server,))
thread_Mqtt.start()