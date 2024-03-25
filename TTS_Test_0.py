from gtts import gTTS 

def speak(text): 
	tts = gTTS(text=text, lang='ko') 
	tts.save('voice.mp3') 

speak("안녕하세요, 저는 IML이에요.")

#파일로 저장한다.