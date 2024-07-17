from gtts import gTTS
import io
import threading
import pygame
import time
import paho.mqtt.client as mqtt
import tkinter as tk
import RPi.GPIO as GPIO

TOPICS = [("fire_detector1/room", 0), ("fire_detector1/fire_alert", 0)]
#토픽을 +/room 과 형태로 변경하면, 모든 화재감지기에서 신호를 받을 수 있다.

server = "3.132.26.214"

stop_flag = False
Fire_locate = None

Fire_Manual_img_path = './fire_manual.jpg'
Evacuate_img_path = './evacuate_plan.jpg'

Button_pin = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def Button_Check():
    global stop_flag
    pre_state = GPIO.input(Button_pin)

    while True:
        cur_state = GPIO.input(Button_pin)

        if(cur_state != pre_state) and (cur_state == GPIO.LOW):
            print("Button Released")
            stop_flag = True
        pre_state = cur_state
        time.sleep(0.5)
    
def on_connect(client, userdata, flags, rc):
    print("Connected with Server" + str(server))

    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global Fire_locate
    global Fire_Manual_img_path

    topic = msg.topic
    message = msg.payload.decode()

    if topic == 'fire_detector1/room':
        pygame.init()

        Fire_locate = message

        Audio_Thread = threading.Thread(target= playAudio, args= (Fire_locate))
        Image_Thread = threading.Thread(target= showImage, args=(Fire_Manual_img_path, Evacuate_img_path))

        Audio_Thread.start()
        Image_Thread.start()

        Audio_Thread.join()
        Image_Thread.join()

        print(message)
    elif topic == "fire_detector1/fire_alert":
        print(message)

        pygame.quit()

def Mqtt_thread(server):
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

def showImage(img1_path, img2_path):
    global stop_flag
    
    win = tk.Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    size = (width, height)

    screen = pygame.display.set_mode(size)
    
    img_1 = pygame.image.load(img1_path)
    img_1 = pygame.transform.scale(img_1, size)

    img_2 = pygame.image.load(img2_path)
    img_2 = pygame.transform.scale(img_2, size)
    
    pygame.display.set_caption("Image Display")

    running = True
    flag = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if flag == 0:
            screen.blit(img_1, (0, 0))
            pygame.display.flip()

        if stop_flag:
            screen.fill((0, 0, 0))
            screen.blit(img_2, (0, 0))
            pygame.display.flip()
            flag = 1

def createTTS(locate):
    text = "현재 화재가 발생한 곳은 {}호 입니다.".format(locate)
    manual = """소화기를 불이 난 곳으로 옮겨주세요.
            손잡이 부분의 안전핀을 뽑아 주세요.
            바람을 등지고 서서 호스를 불쪽으로 향하게 해 주세요.
            손잡이를 힘껏, 움켜쥐고 빗자루로 쓸듯이 뿌려주세요."""
    
    #text = text + manual

    tts = gTTS(text = text, lang = "ko")

    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    return fp