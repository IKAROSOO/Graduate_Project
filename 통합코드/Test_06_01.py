from gtts import gTTS
import io
import threading
import pygame
import time
import paho.mqtt.client as mqtt
from pydub import AudioSegment
from pydub.playback import play

TOPICS = [("topic/locate", 0), ("topic/flags", 0)]

server = "test.mosquitto.org"

global stop_flag
stop_flag = False

global Fire_locate
Fire_locate = None

pygame.init()

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code : " + str(rc))
    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global Fire_locate
    topic = msg.topic
    message = msg.payload.decode()
    if topic == "topic/locate":
        Fire_locate = message
        # 새 위치가 수신될 때마다 TTS를 생성하고 재생합니다.
        createTTS(Fire_locate)

def mqtt_thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(server, 1883, 60)
    client.loop_forever()

def playAudio(audio_data):
    audio = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
    play(audio)

def showImage(img_path):
    screen = pygame.display.set_mode((800, 800))
    img = pygame.image.load(img_path)
    pygame.display.set_caption("Image_Display")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(img, (0, 0))
        pygame.display.flip()
    pygame.quit()

def createTTS(locate):
    text = "현재 화재가 발생한 곳은 {}호 입니다.".format(locate)
    tts = gTTS(text=text, lang="ko")
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    # TTS 오디오를 재생합니다.
    playAudio(fp.read())

img_path = './ヨルシカ.jpg'

thread_Mqtt = threading.Thread(target=mqtt_thread, args=(server,))
thread_ShowImage = threading.Thread(target=showImage, args=(img_path,))

thread_Mqtt.start()
thread_ShowImage.start()
