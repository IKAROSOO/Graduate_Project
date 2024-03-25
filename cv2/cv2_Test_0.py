import cv2
import threading

def showImage(image_path):
    global close_img_flag
    close_img_flag = 0

    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    cv2.imshow("Image", img)

    while True:
        if close_img_flag != 0:
            cv2.destroyAllWindows()
            break

def closeImage():
    global close_img_flag

    close_img_flag = input("Close image : ")

image_path = './manual.jpg'

threading.Thread(target= showImage, args=(image_path,)).start()
threading.Thread(target= closeImage).start()