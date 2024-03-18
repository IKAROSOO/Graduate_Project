import pygame
import time

def show_image(image_path, show_time):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # 화면 크기 설정
    pygame.display.set_caption('Image Display')  # 창 제목 설정

    try:
        img = pygame.image.load(image_path)
        screen.blit(img, (0, 0))  # 이미지를 화면에 표시

        pygame.display.flip()  # 화면 업데이트

        # 지정된 시간동안 이미지 표시
        start_time = time.time()
        while time.time() - start_time < show_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 종료 이벤트
                    return

        pygame.quit()  # Pygame 종료
    except Exception as e:
        print("Error displaying image:", e)

image_path = './ヨルシカ.jpg'
show_time = 5

show_image(image_path, show_time)

#CHat GPT가 작성해준 코드
#matplotlib과 pygame을 동시에 사용하는 것은 오류를 유발할 수 있으므로
#하나의 라이브러리만을 사용하기 위하여 pygmae으로 변경