import threading

global texted_In_flag
texted_In_flag = 0

def Input_Text():
    global texted_In_flag
    text = input('호수를 입력하시오 : ')

    if text != 0:
        texted_In_flag = 0

    return text

def Print_Text(text):
    global texted_In_flag

    if texted_In_flag != 0:
        print('여기는 {}호 입니다'.format(text))

text = Input_Text()

Print_Thread = threading.Thread(target= Print_Text, args= (text, ))

Print_Thread.start()