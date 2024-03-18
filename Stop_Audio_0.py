import pygame
import time

audio_path = './パレード.mp3'

pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

time.sleep(5)

pygame.mixer.music.stop()