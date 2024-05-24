from gtts import gTTS
import io
import threading
import pygame
import time
import paho.mqtt.client as mqtt

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
        playAudio(Fire_locate)

def mqtt_thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, 1883, 60)

    client.loop_forever()

def playAudio(locate):
    if locate is not None:
        buffer = createTTS(locate)
        buffer.seek(0)

        Audio = pygame.mixer.Sound(buffer)
        Audio.play()

        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(0)
        
        Audio.stop()
        del Audio
        buffer.close()

def showImage(img_path):

    screen = pygame.display.set_mode((800, 800))
    img = pygame.image.load(img_path)

    pygame.display.set_caption("Image_Display")

    running = True
    while running:
        screen.blit(img, (0, 0))
        pygame.display.flip()

def createTTS(locate):
    text = "현재 화재가 발생한 곳은 {}호 입니다.".format(locate)
    tts = gTTS(text= text, lang= "ko")

    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    return fp
    
img_path = './ヨルシカ.jpg'

thread_Mqtt = threading.Thread(target= mqtt_thread, args= (server,))
#thread_Audio = threading.Thread(target= playAudio, args= (Fire_locate,))
thread_ShowImage = threading.Thread(target= showImage, args= (img_path, ))

thread_Mqtt.start()
#thread_Audio.start()
thread_ShowImage.start()