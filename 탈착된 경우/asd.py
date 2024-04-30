import paho.mqtt.client as mqtt
import threading
import time

Tact_flag = False   #라즈베리파이가 소화기에 붙어있는 것을 확인하는 TactSwtich. True : 붙어있는 것

def Tact_monitoring():
    global Tact_flag
    
    while True:
        if Tact_flag == False:
            print("라즈베리파이가 탈착됨")
            break
        else:
            time.sleep(1)

    return 0

