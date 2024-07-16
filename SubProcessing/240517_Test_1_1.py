import subprocess
import os
import time

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, '240517_Test_1_2.py')

process = subprocess.Popen(['python', file_path])

time.sleep(3)

process.terminate()