import threading
import pygame
import time
import paho.mqtt.client as mqtt

TOPICS = [("topic/audio", 0), ("topic/img", 0)]

server = "18.116.23.110"       #test.mosquitto.org
                                #18.116.23.110 -> 건희가 만든 서버
global stop_audio_flag
stop_audio_flag = False
global close_img_flag
close_img_flag = False

pygame.init()

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code" + str(rc))

    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global stop_audio_flag
    global close_img_flag

    topic = msg.topic
    message = msg.payload.decode()

    #print(f"Message received from topic {msg.topic}")
    #print(f"Message payload : {msg.payload.decode('utf8')}")

    if topic == "topic/audio":
        print(message)
        if message == "0":
            stop_audio_flag = False
        else:
            stop_audio_flag = True
    elif topic == "topic/img":
        print(message)
        if message == "0":
            close_img_flag = False
        else:
            close_img_flag = True
        close_img_flag = message

def mqtt_thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, 1883, 60)

    client.loop_forever()

def playAudio(audio_path):
    global stop_audio_flag

    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        if stop_audio_flag:
            pygame.mixer.music.stop()
            break
        time.sleep(0.1)
    
def showImage(image_path):  #아직 개선이 필요
    global close_img_flag

    screen = pygame.display.set_mode((800,800))
    img = pygame.image.load(image_path)

    pygame.display.set_caption("Image Display")

    running = True
    while running:
        screen.blit(img, (0, 0))
        pygame.display.flip()

        if close_img_flag == True:
            break

img_path = './ヨルシカ.jpg'
audio_path = './パレード.mp3'


thread_Mqtt = threading.Thread(target= mqtt_thread, args= (server, ))
thread_Audio = threading.Thread(target= playAudio, args= (audio_path, ))
thread_ShowImage = threading.Thread(target= showImage, args= (img_path, ))

thread_Mqtt.start()
thread_Audio.start()
thread_ShowImage.start()

#MQTT와 기존의 오디오, 이미지 코드의 통합본