import threading
import time

i = 1

while True:
    time.sleep(1)

    print("Second : " + str(i))

    i = i + 1 

    if i > 5:
        break

def half_seconds():
    time.sleep(0.5)

    j = 0.5

    while True:
        print("Half Second : " + str(j))

        j = j + 1

        if j > 5:
            break

        time.sleep(1)

Half_Thread = threading.Thread(target= half_seconds)
Half_Thread.start()
