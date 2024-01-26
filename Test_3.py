#실패하였음. -> Thread를 사용하는 것으로 해결이 기대된다.

import time
from PIL import Image

def show_image(img_path, showtime):
    try:
        img = Image.open(img_path)
        img.show()

        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= showtime:
                img.close()
                break
    except Exception as e:
        print(f"Error : {e}")

img_path = "C:/Users/1027a/OneDrive/사진/스크린샷/Fire_Extinghisher_Manual.jpg"
show_image(img_path, 5)