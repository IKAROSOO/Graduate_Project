import tkinter as tk
from PIL import Image, ImageTk
import time
import webview

# 경로 설정
image1_path = r".\AKR20220415091000051_01_i_P4.jpg"
image2_path = r".\20191121111641592dd287-341a-4fe4-90b2-594c1c71da86.jpg"

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
    print(f"Image updated at {time.strftime('%H:%M:%S')}")

# 웹 뷰 보여주기
def show_weather():
    global window
    print("Showing weather at", time.strftime("%H:%M:%S"))
    window = webview.create_window('Weather', 'http://3.132.26.214:8080')
    root.after(10, webview.start)  # 웹뷰를 메인 스레드에서 시작
    root.after(60000, close_weather)  # 1분 후에 웹뷰 닫기 예약

# 웹 뷰 닫기
def close_weather():
    global window
    if window:
        webview.destroy_window(window)
        window = None
        print("Webview closed at", time.strftime("%H:%M:%S"))
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
