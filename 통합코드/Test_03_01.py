from gtts import gTTS


#mqtt  subscibe 하면 []
text = "TTS와 Subprocess의 연동을 하기 위한 테스트 코드입니다."

savepoint = './통합코드/TTS.mp3'

tts = gTTS(text= text, lang='ko')
tts.save(savepoint)      # -> 세이브 경로를 변경하고 싶으면 이름을 설정할 때 경로를 지정해주면 된다.