import threading
import pygame
import time

def Audio(audio_path, play_time):
    try:
        pygame.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        time.sleep(play_time)

        pygame.mixer.music.stop()
    except Exception as e:
        print("Error playing audio:", e)
    finally:
        pygame.mixer.quit()

def showImage(image_path):
    global close_img_flag
    close_img_flag = 0

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Image Display')
    img = pygame.image.load(image_path)

    while True:
        screen.blit(img, (0, 0))
        pygame.display.flip()

        if close_img_flag != 0:
            break
    #기본적으로 사진은 계속 출력이 된다.
    #close_img_flag가 0이 아닌 값이 입력되면 사진 출력이 종료된다.

def closeImage():
    global close_img_flag

    close_img_flag = input("Enter : ")
    #사진을 닫는 것만이 목적인 함수
    #지금은 테스트를 위해 input을 사용했지만, 실제로는 외부 통신을 통하여 close_img_flag를 받아올 예정

img_path = './ヨルシカ.jpg'
audio_path = './パレード.mp3'
play_time = 5

thread_Audio = threading.Thread(target= Audio, args= (audio_path, play_time))
thread_ShowImage = threading.Thread(target= showImage, args= (img_path, ))
thread_CloseImage = threading.Thread(target= closeImage)

thread_Audio.start()
thread_ShowImage.start()
thread_CloseImage.start()