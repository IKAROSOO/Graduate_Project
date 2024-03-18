import threading
import cv2

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
close_flag = 0
showImage(image_path, close_flag)
