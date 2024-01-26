from PIL import Image
import time
import pygame
import sys

topic_Fire = 0
topic_Locate = 0

def When_Fire_happen():
    img_path_manual = "C:/Users/1027a/OneDrive/사진/스크린샷/스크린샷 2024-01-22 161442.png"
    img_path_map = "C:/Users/1027a/OneDrive/사진/스크린샷/스크린샷 2024-01-22 161442.png"
    audio_path = "C:/Users/1027a/Music/천사를_만났어.mp3"

    show_image(img_path_manual)         #소화기의 사용법을 띄워주는 목적
    narrate_manual(audio_path)          #소화기의 사용법의 나레이트
    print("Fire_Flag Success")
    time.sleep(30)
    show_image(img_path_map)            #건물 평면도를 띄워주는 목적
    print("Locate_Flag Success")
    
def show_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Error : {e}")

def narrate_manual(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

print("Enter 'Topic_Fire' : ")
topic_Fire = int(input())

print("Enter 'Topic_Locate' : ")
topic_Locate = int(input())

if topic_Fire == True:
    When_Fire_happen()
    print("Topic_Fire")
elif topic_Locate == True:
    print("Topic_Locate")