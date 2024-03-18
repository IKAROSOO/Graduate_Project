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
    
def showImage(image_path, show_time):
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Image")

    img = pygame.image.load(image_path)
    screen.blit(img, (0, 0))

    pygame.display.flip()

    start_time = time.time()
    while time.time() - start_time < show_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    pygame.quit()

audio_path = './パレード.mp3'
image_path = './ヨルシカ.jpg'
play_time = 5
show_time = 3

thread_Audio = threading.Thread(target= Audio, args= (audio_path, play_time))
thread_Image = threading.Thread(target= showImage, args= (image_path, show_time))

thread_Audio.start()
thread_Image.start()