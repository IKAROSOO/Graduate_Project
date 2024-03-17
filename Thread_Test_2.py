import threading
import time
from PIL import Image
import pygame

def play_audio(audio_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error Audio by : ", e)
    finally:
        pygame.mixer.quit()
        pygame.quit()

def show_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print("Error Image by : ", e)

audio_path = './パレード.mp3'
image_path = './ヨルシカ.jpg'

therad_Audio = threading.Thread(target= play_audio, args= (audio_path,))
thread_Image = threading.Thread(target= show_image, args= (image_path,))

#Thread에 함수의 인자를 제공할 때, 인수가 1개여도 마지막에 ','를 붙여야 정상 작동한다.
#Thread는 함수의 인자를 Tuple로만 제공해야만 하기 때문이다.

thread_Image.start()
therad_Audio.start()

#Audio와 Image가 동시에 나오는 것까지 성공