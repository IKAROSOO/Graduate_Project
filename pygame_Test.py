import pygame

audio_path = "C:/Users/1027a/Music/천사를_만났어.mp3"

pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)