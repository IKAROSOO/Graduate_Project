import threading
import pygame
import time
import paho.mqtt.client as mqtt

def playAudio(audio_path):
    global stop_audio_flag
    stop_audio_flag = 0

    pygame.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    if stop_audio_flag != 0:
        pygame.mixer.music.stop()
        pygame.quit()

def stopAudio():
    global stop_audio_flag

    time.sleep(10)

    stop_audio_flag = 1

def showImage(image_path):
    global close_img_flag
    close_img_flag = 0

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    img = pygame.image.load(image_path)

    pygame.display.set_caption('Image Display')

    while True:
        screen.blit(img, (0, 0))
        pygame.display.flip()

        if close_img_flag != 0:
            pygame.quit()
            break

def closeImage():
    global close_img_flag

    close_img_flag = input("Close Image : ")

img_path = './ヨルシカ.jpg'
audio_path = './パレード.mp3'

thread_Audio = threading.Thread(target= playAudio, args= (audio_path, ))
thread_ShowImage = threading.Thread(target= showImage, args= (img_path, ))
thread_CloseImage = threading.Thread(target= closeImage)
thread_StopAudio = threading.Thread(target= stopAudio)

thread_Audio.start()
thread_ShowImage.start()
thread_CloseImage.start()
thread_StopAudio.start()

#키를 입력하면 Audio와 Image가 동시에 종료됨
#이유는 모르겠다