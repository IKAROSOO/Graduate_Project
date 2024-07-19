from gtts import gTTS
import io
import sys
import threading
import pygame
import time
import paho.mqtt.client as mqtt
import tkinter as tk

try:
    Recived_Room = sys.argv[1]
except ValueError:
    print("NO RECEIVED DATA")

Evacuate_img_path = './evacuate_plan.jpg'

def playAudio(locate):
    if locate is not None:
        while True:
            buffer = createTTS(locate)
            buffer.seek(0)

            Audio = pygame.mixer.Sound(buffer)
            Audio.play()

            while pygame.mixer.get_busy():
                pygame.time.Clock().tick(0)
            
            Audio.stop()

            del Audio
            buffer.close()

            time.sleep(10)

def showImage(img1_path):
    win = tk.Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    size = (width, height)

    screen = pygame.display.set_mode(size)
    
    img_1 = pygame.image.load(img1_path)
    img_1 = pygame.transform.scale(img_1, size)
    
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

def createTTS(locate):
    text = f"현재 화재가 발생한 곳은 {locate}호 입니다."
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

Image_Thread = threading.Thread(target= showImage, args=(Evacuate_img_path, ))
Audio_Thread = threading.Thread(target= playAudio, args=(Recived_Room, ))

Image_Thread.start()
Audio_Thread.start()