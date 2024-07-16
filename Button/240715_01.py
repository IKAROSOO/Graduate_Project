import RPi.GPIO as GPIO
import time

global Button_flag
Button_flag = False

Button_pin = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.setup(channel, mode, pull_up_down= ~, initial=None)
#channel : 내가 선택할 버튼
#mode : 입력을 할 지 출력을 할 지 선택
#pull_up_down : 입력의 경우, 풀업이나 풀다운 저항을 설정
#풀업으로 설정 시 : 기본적으로 HIGH
#풀다운으로 설정 시 : 기본적으로 LOW

#initial : 출력의 경우, HIGH로 할 지 LOW로 할 지 설정

def Button_check():
    pre_state = GPIO.input(Button_pin)

    while True:
        cur_state = GPIO.input(Button_pin)

        if (cur_state != pre_state) and (cur_state == GPIO.LOW):
            print("Button Released")

        pre_state = cur_state
        time.sleep(0.5)