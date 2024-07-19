import os
import sys
import time
import paho.mqtt.client as mqtt
import threading
import tkinter as tk
import webview
from PIL import Image, ImageTk

fire_alert_file = os.path.dirname(os.path.abspath(__file__))

image1_path = os.path.join(fire_alert_file, "evacuate_plan.jpg")
image2_path = os.path.join(fire_alert_file, "fire_manual.jpg")

TOPICS = [("+/room", 0), ("+/fire_alert", 0)]

server = "3.132.26.214"

Room = None

root = tk.Tk()
root.title("Weather App")

photo = None
window = None

win = tk.Tk()
win.withdraw()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win_size = (width, height)
win.destroy()

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code : " + str(rc))
    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global Room
    topic = msg.topic
    message = msg.payload.decode()
    print(f"\n\n\n{message}\n\n\n")

    if topic.endswith("/room"):
        Room = message
    elif topic.endswith("/fire_alert"):
        print("Fire Outbreaked!!")
        stop_process()

def mqtt_Thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(server, 1883, 60)
    client.loop_forever()

def stop_process():
    global window
    global Room

    # 모든 창을 닫고 Tkinter 루프를 종료
    if window:
        window.destroy()
    root.quit()

    # 새 스크립트를 실행
    os.system(f"python3 240719_Test_1_2.py {Room}")
    
    # 프로세스 종료
    sys.exit()

def display_image(image_path):
    global photo
    img = Image.open(image_path)
    img = img.resize(win_size, Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label.configure(image=photo)
    label.image = photo

def show_weather():
    global window
    root.withdraw()
    label.pack_forget()
    window = webview.create_window("Weather", "http://3.132.26.214:8080", width=width, height=height)
    webview.start(destroy_weather, window)

def destroy_weather(window):
    time.sleep(5)
    window.destroy()
    label.pack(padx=10, pady=10)
    root.deiconify()
    root.after(0, job_image1)

def job_image1():
    print("Displaying image {} at ".format(image1_path), time.strftime("%H : %M : %S"))
    display_image(image1_path)
    root.after(5000, job_image2)

def job_image2():
    print("Displaying image {} at ".format(image2_path), time.strftime("%H : %M : %S"))
    display_image(image2_path)
    root.after(5000, schedule_show_weather)

def schedule_show_weather():
    print("Scheduling webview at", time.strftime("%H : %M : %S"))
    root.after(5000, show_weather)

def normal_routine():
    job_image1()

label = tk.Label(root)
label.pack(padx=10, pady=10)

Thread_Mqtt = threading.Thread(target=mqtt_Thread, args=(server,))
Thread_Mqtt.start()

root.after(0, normal_routine)
root.mainloop()
