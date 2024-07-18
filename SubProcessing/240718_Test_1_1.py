import subprocess

file_path = "240718_Test_1_2.py"

test_value = "604호"
command = ["python", file_path, test_value]

result = subprocess.run(command, capture_output=True, text=True)

print("stdout : ", result.stdout)
print("stderr : ", result.stderr)