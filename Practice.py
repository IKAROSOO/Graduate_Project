import threading
import time
import pygame

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
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Image Display')

    img = pygame.image.load(image_path)
    screen.blit(img, (0, 0))

    pygame.display.flip()

    while close_img_flag == 0:
        Key_capture()
        
        if close_img_flag != 0:
            break
                                          
def Key_capture():
    global close_img_flag
    close_img_flag = input("Press Enter to close the image : ")                        

close_img_flag = 0

img_path = './ヨルシカ.jpg'
audio_path = './パレード.mp3'
play_time = 5

thread_Audio = threading.Thread(target= Audio, args=(audio_path, play_time))
thread_Image = threading.Thread(target= showImage, args=(img_path, ))

thread_Audio.start()
thread_Image.start()

thread_Audio.join()
thread_Image.join()