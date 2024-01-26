import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")
        # 일정 부분까지 실행되면 다른 쓰레드를 실행
        if i == 2:
            event.set()

def print_letters():
    # event가 설정될 때까지 대기
    event.wait()
    for letter in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {letter}")

# 이벤트 객체 생성
event = threading.Event()

# 쓰레드 생성
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 쓰레드 시작
thread1.start()
thread2.start()

# 모든 쓰레드가 종료될 때까지 대기
thread1.join()
thread2.join()

print("모든 쓰레드 종료")
