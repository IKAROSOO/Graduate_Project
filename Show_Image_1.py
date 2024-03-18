import threading
import time
from PIL import Image

def show_Image(image_path, show_time):
    try:
        image = Image.open(image_path)
        image.show()

        time.sleep(show_time)

        image.close()
    except Exception as e:
        print("Error Image by : ", e)

def Timer(play_time):
    i = 0

    for i in range(play_time):
        print("Time : {} Second".format(i))
        i = i + 1
        time.sleep(1)

image_path = './ヨルシカ.jpg'
show_time = 5

thread_Image = threading.Thread(target= show_Image, args= (image_path, show_time))
thread_Timer = threading.Thread(target= Timer, args= (show_time,))

thread_Image.start()
thread_Timer.start()

thread_Image.join()
thread_Timer.join()

#실패
#Thread는 작동하지만, 사진이 마지막까지 종료되지 않음