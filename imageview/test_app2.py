import tkinter as tk
from PIL import Image, ImageTk
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

# 이미지 표시를 위한 함수
def display_image(image_path):
    global photo
    # 이미지 열기 및 리사이징
    img = Image.open(image_path)
    img = img.resize((800, 480), Image.LANCZOS)  # 이미지 사이즈 조정 (LANCZOS 사용)
    # PhotoImage 업데이트
    photo = ImageTk.PhotoImage(img)
    # 이미지 라벨 업데이트
    label.configure(image=photo)
    label.image = photo  # 참조 유지
    print(f"Image updated at {time.strftime('%H:%M:%S')}")

# 웹 뷰 보여주기
def show_weather():
    global window
    root.withdraw()  # Tkinter 창 숨기기
    print("Showing weather at", time.strftime("%H:%M:%S"))
    label.pack_forget()  # 이미지 라벨 숨기기
    window = webview.create_window('Weather', 'http://3.132.26.214:8080', width=800, height=480)
    webview.start(destroy, window)

# 웹 뷰 닫기
       
def destroy(window):
    # show the window for a few seconds before destroying it:
    time.sleep(60)
    window.destroy()
    print("Webview closed at", time.strftime("%H:%M:%S"))
    label.pack(padx=10, pady=10)  # 이미지 라벨 다시 표시
    root.deiconify()  # Tkinter 창 다시 표시
    root.after(0, job_image1)  # 웹뷰 닫힌 후 이미지 1 표시

# 순차적으로 작업을 실행하는 함수들
def job_image1():
    print("Displaying image 1 at", time.strftime("%H:%M:%S"))
    display_image(image1_path)
    root.after(60000, job_image2)  # 1분(60000ms) 후에 이미지 2를 표시

def job_image2():
    print("Displaying image 2 at", time.strftime("%H:%M:%S"))
    display_image(image2_path)
    root.after(60000, schedule_show_weather)  # 1분(60000ms) 후에 웹뷰를 표시

def schedule_show_weather():
    print("Scheduling webview at", time.strftime("%H:%M:%S"))
    root.after(0, show_weather)

# 이미지를 표시할 라벨 생성
label = tk.Label(root)
label.pack(padx=10, pady=10)

# 초기에 이미지1 표시
job_image1()

# Tkinter 루프 시작
root.mainloop()
