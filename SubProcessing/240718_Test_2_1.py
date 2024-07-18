from PIL import Image, ImageTk
import os
import subprocess
import time
import paho.mqtt.client as mqtt
import threading
import tkinter as tk
import webview

fire_alert_file = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(fire_alert_file, '240718_Test_2_2.py')

image1_path = os.path.join(fire_alert_file, "evacuate_plan.jpg")
image2_path = os.path.join(fire_alert_file, "fire_manual.jpg")

TOPICS = [("+/room", 0), ("+/fire_alert", 0)]

server = "3.132.26.214"

Room = None
#화재가 난 곳의 방 호수

#switch_process = False
#사용할 이유가 사라지면서 주석처리
#def on_message에 있는 switch_process 또한 주석처리

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
    #global switch_process
    global Room

    topic = msg.topic
    message = msg.payload.decode()
    

    if topic.endswitch("/room"):
        Room = message
    elif topic.endswitch("/fire_alert"):
        print("Fire Outbreaked!!")

        stop_process()

def mqtt_Thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, 1883, 60)

    client.loop_forever()

#MQTT가 들어왔을 때 전부 종료하는 함수
def stop_process():
    global window
    global Room

    root.withdraw()
    if window:
        window.destroy()
    
    command = ["python", file_path, Room]
    subprocess.run(command, capture_output=True, text=True)

#이미지 표시를 위한 함수
def display_image(image_path):
    global photo

    img = Image.open(image_path)
    img = img.resize(win_size, Image.LANCZOS)

    photo = ImageTk.PhotoImage(img)

    label.configure(image=photo)
    label.image = photo

#웹 뷰 표시를 위한 함수
def show_weather():
    global window
    
    root.withdraw()    
    label.pack_forget()
    window = webview.create_window("Weather", "http://3.132.26.214:8080", width= width, height= height)
    webview.start(destroy_weather, window)

#웹 뷰 종료를 위한 함수
def destroy_weather(window):
    #매개변수가 반드시 존재해야 한다.
    global image1_path

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

def noraml_routine():
    job_image1()

label = tk.Label(root)
label.pack(padx=10, pady=10)

Thread_Mqtt = threading.Thread(target= mqtt_Thread, args= (server,))
Thread_Mqtt.start()

root.after(0, noraml_routine)
root.mainloop()