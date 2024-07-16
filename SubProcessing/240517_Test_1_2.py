import time

i = 1

while True:
    print("Seconds : " + str(i))

    i=i+1
    #time.sleep(1)
    
    if i > 10:
        break

print("process End")