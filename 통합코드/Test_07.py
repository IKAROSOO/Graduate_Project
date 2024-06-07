from gtts import gTTS
import io
import threading
import pygame
import time
import paho.mqtt.client as mqtt
import tkinter as tk

TOPICS = [("topic/locate", 0), ("topic/flags", 0)]

server = "18.116.23.110"

global stop_flag
stop_flag = False

global Fire_locate
Fire_locate = None

global Fire_Manual_img_path
Fire_Manual_img_path = './Fire_Manual.png'

global Plan_img_path
Plan_img_path = './Plan.png'

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code : " + str(rc))

    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global Fire_locate
    global Fire_Manual_img_path
    global Plan_img_path

    topic = msg.topic
    message = msg.payload.decode()

    if topic == "topic/locate":
        pygame.init()

        Fire_locate = message

        stop_event = threading.Event()

        Audio_Thread = threading.Thread(target= playAudio, args= (Fire_locate, stop_event))
        Image_Thread = threading.Thread(target= showImage, args= (Fire_Manual_img_path, stop_event ,
                                                                  Plan_img_path))

        Audio_Thread.start()
        Image_Thread.start()

        Audio_Thread.join()
        Image_Thread.join()

        print(message)
    elif topic == "topic/flags":
        print(message)
        
        pygame.quit()

def mqtt_thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, 1883, 60)

    client.loop_forever()

def playAudio(locate, stop_event):
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
    
        stop_event.set()

def showImage(First_img_path, stop_event, Seconde_img_path):
    win = tk.Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    size = (width,height)
    
    screen = pygame.display.set_mode(size)
    img = pygame.image.load(First_img_path)
    img = pygame.transform.scale(img, size)
    
    img_1 = pygame.image.load(Seconde_img_path)
    img_1 == pygame.transform.scale(img_1, size)
    pygame.display.set_caption("Image_Display")

    running = True
    flag__= 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if flag__ == 0:
            screen.blit(img, (0, 0))
            pygame.display.flip()

        if stop_event.is_set():
            screen.fill((0, 0, 0))
            screen.blit(img_1, (0, 0))
            pygame.display.flip()
            flag__ = 1

def createTTS(locate):
    text = "현재 화재가 발생한 곳은 {}호 입니다.".format(locate)
    manual = """소화기를 불이 난 곳으로 옮겨주세요.
            손잡이 부분의 안전핀을 뽑아 주세요.
            바람을 등지고 서서 호스를 불쪽으로 향하게 해 주세요.
            손잡이를 힘껏, 움켜쥐고 빗자루로 쓸듯이 뿌려주세요."""
    
    #text = text + manual

    tts = gTTS(text= text, lang= "ko")

    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    return fp

thread_Mqtt = threading.Thread(target= mqtt_thread, args= (server,))
#thread_Audio = threading.Thread(target= playAudio, args= (Fire_locate,))
#thread_ShowImage = threading.Thread(target= showImage, args= (img_path, ))

thread_Mqtt.start()
#thread_Audio.start()
#thread_ShowImage.start()