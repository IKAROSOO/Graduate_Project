from gtts import gTTS

def speak(text):
    tts = gTTS(text= text, lang= 'ko')
    tts.save('Test_00.mp3')

Test_str = '여기는 {}호 입니다.'

print(Test_str.format(101))