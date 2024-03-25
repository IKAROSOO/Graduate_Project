import threading
import pygame
import time

def playAudio(audio_path):
    global stop_audio_flag
    stop_audio_flag = 0

    pygame.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    if stop_audio_flag != 0:
        pygame.mixer.music.stop()

def stopAudio():
    global stop_audio_flag
    
    time.sleep(10)

    stop_audio_flag = 1

def showImage(image_path):
    global close_img_flag
    close_img_flag = 0

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    img = pygame.image.load(image_path)

    pygame.display.set_caption("Image Display")

    while True:
        screen.blit(img, (0, 0))
        pygame.display.flip()

        if close_img_flag != 0:
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

#이미지와 오디오 전부 pygame라이브러리만으로 작동

#기존까지 실패하던 이유
# 1. 사진이 먼저 종료될 때 if문에 pygame.quit()이 들어가 있어서
# 2. pygame전체가 종료되기 때문에 오디오도 정지되어 버린다.