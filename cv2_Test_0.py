import cv2
import time

def showImage(image_path, show_time):
    try:
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        cv2.imshow("Image", img)

        cv2.waitKey(show_time * 1000)
    finally:
        cv2.destroyAllWindows()

image_path = './manual.jpg'
show_time = 3

showImage(image_path, show_time)