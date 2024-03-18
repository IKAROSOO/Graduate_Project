import threading
import pygame
import time

def Audio(audio_path, play_time):
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        time.sleep(play_time)

        pygame.mixer.music.stop()
    except Exception as e:
        print("Error Audio by : ", e)
    finally:
        pygame.mixer.quit()

#Aduio 함수만으로 음악의 재생 중단이 성공

def Timer(play_time):
    i = 0

    for i in range(play_time):
        print("Time : {} Second".format(i))
        i = i + 1
        time.sleep(1)

#Timer 함수는 Thread기능 연습과, 시간의 흐름을 확인하는 용도

audio_path = './パレード.mp3'
play_time = 5

thread_Audio = threading.Thread(target= Audio, args= (audio_path, play_time))
thread_Timer = threading.Thread(target= Timer, args= (play_time,))

thread_Audio.start()
thread_Timer.start()