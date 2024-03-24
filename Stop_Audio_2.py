import threading
import pygame

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

    stop_audio_flag = input("Stop audio : ")

audio_path = './パレード.mp3'

thread_playAudio = threading.Thread(target= playAudio, args= (audio_path, ))
thread_stopAudio = threading.Thread(target= stopAudio)

thread_playAudio.start()
thread_stopAudio.start()

#시간으로 음성을 멈추는 것이 아닌 stop_audio_flag가 0이 아닌 값이 입력되면 음성 종료된다.