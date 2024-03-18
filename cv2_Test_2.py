import threading
import cv2

# 이미지 표시 함수
def show_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.imshow("Image", img)

# 키 입력을 받는 함수
def key_capture_thread(close_flag):
    input("Press Enter to close the image...")

    # 입력이 들어오면 close_flag를 1로 변경하여 이미지를 종료하도록 함
    close_flag[0] = 1

def main():
    image_path = './manual.jpg'
    close_flag = [0]  # 리스트를 사용하여 mutable한 객체로 전달

    # 이미지 표시
    show_image(image_path)

    # 키 입력을 받는 스레드 시작
    threading.Thread(target=key_capture_thread, args=(close_flag,)).start()

    # close_flag가 0일 때까지 대기
    while close_flag[0] == 0:
        cv2.waitKey(100)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
