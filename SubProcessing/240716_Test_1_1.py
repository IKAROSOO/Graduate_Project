from PIL import Image, ImageTk
import os
import subprocess
import time
import paho.mqtt.client as mqtt
import threading
import tkinter as tk
import webview

fire_alert_file = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(fire_alert_file, '240716_Test_1_2.py')

image1_path = "evacuate_plan.jpg"
image2_path = "fire_manual.jpg"

TOPICS = [("+/fire_alert", 0)]

server = "3.132.26.214"

#switch_process = False
#사용할 이유가 사라지면서 주석처리
#def on_message에 있는 switch_process 또한 주석처리

root = tk.Tk()
root.title("Weather App")

photo = None
window = None

def on_connect(client, userdata, flags, rc):
    print("Connected with Result Code : " + str(rc))
    client.subscribe(TOPICS)

def on_message(client, userdata, msg):
    global switch_process

    topic = msg.topic
    message = msg.payload.decode()

    if topic == "+/fire_alert":
        print("Fire Outbreaked!!")

        #switch_process = True
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
    if window:
        window.destroy()
    
    root.quit()

    subprocess.Popen(["python", file_path])

#이미지 표시를 위한 함수
def display_image(image_path):
    global photo

    img = Image.open(image_path)
    img = img.resize((800, 480), Image.LANCZOS)

    photo = ImageTk.PhotoImage(img)

    label.configure(image=photo)
    label.image = photo

#웹 뷰 표시를 위한 함수
def show_weather():
    global window
    root.withdraw()
    
    label.pack_forget()
    window = webview.create_window("Weather", "http://3.132.26.214:8080", width = 800, height = 480)
    webview.start(destroy_weather, window)

#웹 뷰 종료를 위한 함수
def destroy_weather():
    global image1_path

    time.sleep(30)
    window.destroy()

    label.pack(padx=10, pady=10)
    root.deiconify()
    root.after(0, job_image1)

def job_image1():
    print("Displaying image {} at ".format(image1_path), time.strftime("%H : %M : %S"))
    display_image(image1_path)
    root.after(30000, job_image2)

def job_image2():
    print("Displaying image {} at ".format(image2_path), time.strftime("%H : %M : %S"))
    display_image(image2_path)
    root.after(30000, schedule_show_weather)

def schedule_show_weather():
    print("Scheduling webview at", time.strftime("%H : %M : %S"))
    root.after(30000, show_weather)

def noraml_routine():
    job_image1()

Thread_Mqtt = threading.Thread(target= mqtt_Thread, args= (server,))
Thread_Mqtt.start()

root.after(0, noraml_routine)
root.mainloop()