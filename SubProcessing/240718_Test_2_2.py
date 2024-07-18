from gtts import gTTS
import io
import sys
import threading
import pygame
import time
import paho.mqtt.client as mqtt
import tkinter as tk

#Recived_Room = sys.argv[1]

stop_flag = False

Fire_Manual_img_path = './fire_manual.jpg'
Evacuate_img_path = './evacuate_plan.jpg'

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

