import subprocess
import os

num = input()

Test_path = os.path.join('240716_Test_1_1.py')

if num == True:
    subprocess.Popen(['python', Test_path])
else:
    print("히히")