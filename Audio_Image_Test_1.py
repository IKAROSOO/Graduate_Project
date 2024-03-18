import threading
import time
import pygame
import cv2

def Audio(audio_path, play_time):
    try:
        pygame.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        time.sleep(play_time)
        #play_time의 시간만큼 다음 코드의 실행을 지연시킴.

        pygame.mixer.music.stop()
    finally:
        pygame.mixer.quit()
        #최종적으로는 모든 Audio는 종료된다.

def showImage(image_path, show_time):
    try:
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        cv2.imshow('Image', img)

        cv2.waitKey(show_time * 1000)
        #위의 함수는 ms단위로 동작 -> *1000을 해서 s단위로 변경
        #show_time의 시간 후 이미지가 종료된다.
    finally:
        cv2.destroyAllWindows()

image_path = './manual.jpg'
audio_path = './パレード.mp3'
show_time = 3
play_time = 10

thread_Audio = threading.Thread(target= Audio, args=(audio_path, play_time))
thread_Image = threading.Thread(target= showImage, args= (image_path, show_time))

thread_Audio.start()
thread_Image.start()