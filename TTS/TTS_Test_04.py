from gtts import gTTS
import pygame
import io

# 텍스트를 음성으로 변환
text = "테스트용"
tts = gTTS(text=text, lang='ko')

# 변환된 음성을 메모리 버퍼에 저장
fp = io.BytesIO()
tts.write_to_fp(fp)
fp.seek(0)

# pygame을 사용하여 음성 재생
#pygame.mixer.init()
#pygame.mixer.music.load(fp)
#pygame.mixer.music.play()

# 재생이 끝날 때까지 기다림
#while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(10)
