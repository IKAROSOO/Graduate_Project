from PIL import Image
from io import BytesIO
import paho.mqtt.client as mqtt

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
        print(f"에러: {e}")

client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()