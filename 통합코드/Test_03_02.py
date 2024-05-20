import Test_03_01 as tts
import pygame

pygame.init()

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

savepoint = tts.savepoint

playAudio(savepoint)

#import 파일명을 통하여 해당 파일을 실행시킬 수 있고,
#해당 파일에 있던 변수들을 끌어올 수 있다.