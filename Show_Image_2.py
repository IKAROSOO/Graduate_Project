import multiprocessing
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
    for i in range(play_time):
        print("Time : {} Second".format(i))
        time.sleep(1)

if __name__ == "__main__":
    image_path = './ヨルシカ.jpg'
    show_time = 5

    process_Image = multiprocessing.Process(target= show_Image, args= (image_path, show_time))
    process_Timer = multiprocessing.Process(target= Timer, args= (show_time,))

    process_Image.start()
    process_Timer.start()

    process_Image.join()
    process_Timer.join()

#실패
#Chat GPT가 작성해준 코드