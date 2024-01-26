import paho.mqtt.client as mqtt
from PIL import Image

def on_connect(client, usedata, flags, rc):
    print("Connected with Result Code " + str(rc))
    client.subscribe("mqtt/topic")

def on_message(client, userdata, msg):
    print("Received Message")
    image_path = "C:/Users/1027a/OneDrive/사진/스크린샷/스크린샷 2024-01-22 161442.png"
    show_image(image_path)

def show_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Error : {e}")

def set_image_path(message):    #Message의 형태를 미리 정해서 몇층에서 불이 났는지 구분할 수 있도록 한다.
    

client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

client.connect("Enter Srever IP Address", 1883, 60)

client.loop_forever()