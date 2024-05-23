import TTS_Test_04 as TTS
import pygame

buffer = TTS.fp

pygame.mixer.init()
pygame.mixer.music.load(buffer)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)