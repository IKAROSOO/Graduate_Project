from PIL import Image
import os

def show_image(image_path):
    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print("Error by :", e)

image_path = './ヨルシカ.jpg'
show_image(image_path)

#Only Show Image, Can't close the Image