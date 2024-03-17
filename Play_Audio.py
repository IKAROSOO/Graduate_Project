import pygame

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error by : ", e)
    finally:
        pygame.mixer.quit()
        pygame.quit()

play_audio('./パレード.mp3')

#Only play Audio, Can't stop the audio