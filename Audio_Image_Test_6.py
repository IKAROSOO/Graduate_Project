import threading
import pygame
import cv2
import time

def playAudio(audio_path):
    global stop_audio_flag
    stop_audio_flag = 0

    pygame.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while True:
        if stop_audio_flag != 0:
            pygame.mixer.music.stop()
            pygame.quit()
            break

def stopAudio():
    global stop_audio_flag
    
    time.sleep(7)
    
    stop_audio_flag = 1

def showImage(image_path):
    global close_img_flag
    close_img_flag = 0
    
    img = cv2.imread(image_path)
    cv2.imshow("Image", img)
    cv2.waitKey(0)

    while not close_img_flag:
        pass

    cv2.destroyAllWindows()        

def closeImage():
    global close_img_flag
    
    input("Enter to Close Image : ")
    close_img_flag = True

img_path = './manual.jpg'
audio_path = './パレード.mp3'

thread_playAduio = threading.Thread(target= playAudio, args= (audio_path,))
thread_stopAudio = threading.Thread(target= stopAudio)
thread_showImage = threading.Thread(target= showImage, args= (img_path, ))
thread_closeImage = threading.Thread(target= closeImage)

thread_playAduio.start()
thread_stopAudio.start()
thread_showImage.start()
thread_closeImage.start()