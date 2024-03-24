import cv2
import threading

def showImage(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.imshow('Image', img)

def keyCapture():
    # ESC 키가 눌릴 때까지 대기
    while True:
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

img_path = './manual.jpg'

# 이미지 표시 스레드 시작
image_thread = threading.Thread(target=showImage, args=(img_path,))
key_thread = threading.Thread(target=keyCapture)

image_thread.start()
key_thread.start()

# 키 입력 처리 스레드 시작

# 메인 스레드는 다른 작업 수행 가능
