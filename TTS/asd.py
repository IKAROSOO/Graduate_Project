from gtts import gTTS
import os

input_text = input("Enter the text you want to convert to speech: ")

tts = gTTS(text= input_text, lang='ko')

tts.save("TTS_test_00.mp3")

os.system("TTS_test_00.mp3")