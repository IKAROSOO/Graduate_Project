import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

def show_image(image_path, duration):
    # 이미지 열기
    img = mpimg.imread(image_path)
    imgplot = plt.imshow(img)
    plt.axis('off')  # 축 제거

    # 이미지 창 유지 및 대기
    plt.show(block=False)
    plt.pause(duration)

    # 이미지 창 닫기
    plt.close()

if __name__ == "__main__":
    # 이미지 파일 경로
    image_path = './ヨルシカ.jpg'

    # 표시할 시간(초)
    display_duration = 3

    # 이미지 표시
    show_image(image_path, display_duration)


#성공, 하지만 cv2로 시도해봤지만 이상한 에러 발생
#Chat GPT가 작성해준 코드