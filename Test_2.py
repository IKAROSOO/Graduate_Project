#정해진 시간 이후에 나레이터가 정지

import pygame
import time

def narrate_manual(audio_path, playtime):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    start_time = time.time()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

        # 일정 시간이 지나면 음악 정지
        elapsed_time = time.time() - start_time
        if elapsed_time >= playtime:
            pygame.mixer.music.stop()
            break

audio_path = "C:/Users/1027a/Music/천사를_만났어.mp3"
play_duration = 10  # 재생할 시간 (초)
narrate_manual(audio_path, play_duration)
