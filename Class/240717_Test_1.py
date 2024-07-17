from PIL import Image, ImageTk
import tkinter as tk
import time
import os
import webview

script_dir = os.path.dirname(__file__)

# 경로 설정
image1_path = "./evacuate_plan.jpg"
image2_path = "./fire_manual.jpg"

# Tkinter 애플리케이션 생성
root = tk.Tk()
root.title("Weather App")

# 전역 변수로 PhotoImage 객체 생성
photo = None
window = None

class DisplayView:
    def display_image(image_path):
        win = tk.Tk()
        width = win.winfo_screenwidth()
        height = win.winfo_screenheight()
        size = (width, height)

        img = Image.open(image_path)
        img = img.resize(size, Image.LANCZOS)

        photo = ImageTk.PhotoImage(img)

        label.configure(image=photo)
        label.image = photo
        print(f"Image updated at {time.strftime("%H:%M:%S")}")

    def ImageView(image_path):
        print("Displaying Image", time.strftime("%H:%M:%S"))
        display_image(image_path)



#Failed 24_07_17_19:47