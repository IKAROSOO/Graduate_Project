from PIL import Image, ImageTk
from gtts import gTTS
import os
import time
import pygame
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

    print(f"\n\n\n{message}\n\n\n")    

    if topic.endswith("/room"):
        Room = message
    elif topic.endswith("/fire_alert"):
        print("Fire Outbreaked!!")

        Image_Thread = threading.Thread(target= showImage, args=(image1_path))
        Audio_Thread = threading.Thread(target= playAudio, args=(Room))

        Image_Thread.start()
        Audio_Thread.start()
    
def mqtt_Thread(server):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server, 1883, 60)

    client.loop_forever()

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

#-----------위에는 SUbprocessing의 1번 코드

def playAudio(locate):
    if locate is not None:
        while True:
            buffer = createTTS(locate)
            buffer.seek(0)

            Audio = pygame.mixer.Sound(buffer)
            Audio.play()

            while pygame.mixer.get_busy():
                pygame.time.Clock().tick(0)
            
            Audio.stop()

            del Audio
            buffer.close()

            time.sleep(10)

def showImage(img1_path):
    win = tk.Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    size = (width, height)

    screen = pygame.display.set_mode(size)
    
    img_1 = pygame.image.load(img1_path)
    img_1 = pygame.transform.scale(img_1, size)
    
    pygame.display.set_caption("Image Display")

    running = True
    flag = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if flag == 0:
            screen.blit(img_1, (0, 0))
            pygame.display.flip()

def createTTS(locate):
    text = f"현재 화재가 발생한 곳은 {locate}호 입니다."
    manual = """소화기를 불이 난 곳으로 옮겨주세요.
            손잡이 부분의 안전핀을 뽑아 주세요.
            바람을 등지고 서서 호스를 불쪽으로 향하게 해 주세요.
            손잡이를 힘껏, 움켜쥐고 빗자루로 쓸듯이 뿌려주세요."""
    
    #text = text + manual

    tts = gTTS(text = text, lang = "ko")

    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    return fp



label = tk.Label(root)
label.pack(padx=10, pady=10)

Thread_Mqtt = threading.Thread(target= mqtt_Thread, args= (server,))
Thread_Mqtt.start()

root.after(0, noraml_routine)
root.mainloop()