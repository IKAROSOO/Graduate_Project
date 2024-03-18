import threading
import time
import pygame
import cv2

close_flag = 0


def Audio(audio_path, play_time):
    try:
        pygame.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        time.sleep(play_time)
        #play_time의 시간만큼 다음 코드의 실행을 지연시킴.

        pygame.mixer.music.stop()
    finally:
        pygame.mixer.quit()
        #최종적으로는 모든 Audio는 종료된다.

def showImage(image_path, close_flag):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.imshow("Image", img)

    # 키 입력을 받기 위한 함수
    def key_capture_thread():
        nonlocal close_flag
        input("Press Enter to close the image...")

        # 입력이 들어오면 close_flag를 1로 변경하여 이미지를 종료하도록 함
        close_flag = 1

    # 키 입력을 받는 스레드 시작
    threading.Thread(target=key_capture_thread).start()

    # close_flag가 0이 아니면 이미지 종료
    while close_flag == 0:
        cv2.waitKey(1)

    cv2.destroyAllWindows()

image_path = './manual.jpg'
audio_path = './パレード.mp3'
play_time = 10

thread_Audio = threading.Thread(target= Audio, args=(audio_path, play_time))
thread_Image = threading.Thread(target= showImage, args= (image_path, close_flag))

thread_Audio.start()
thread_Image.start()