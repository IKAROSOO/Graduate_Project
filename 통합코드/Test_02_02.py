import Test_02_01 as tts
import pygame

pygame.init()

savepoint = tts.savepoint

def playAudio(audio_path):
    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error by : ", e)
    finally:
        pygame.mixer.quit()
        pygame.quit()

print(savepoint)