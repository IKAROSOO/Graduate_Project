from PIL import Image
import time

image_path = './ヨルシカ.jpg'
show_time = 3

image = Image.open(image_path)
image.show()

time.sleep(show_time)

image.close()

#실패
#여전히 이미지의 출력 후, 종료가 되지 않는다.