import threading
import time

def print_number1(Num):
    for i in range(Num):
        time.sleep(1)
        print(f"Thread 1 : {i}")

def print_number2(Num):
    for i in range(Num):
        time.sleep(1)
        print(f"Thread 2 : {10*i}")

thread1 = threading.Thread(target=print_number1(5))
thread2 = threading.Thread(target=print_number2(5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All Thread End!")