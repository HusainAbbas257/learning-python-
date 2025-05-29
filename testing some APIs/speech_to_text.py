import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "What?"

if(__name__=='__main__'):
    text=''
    while(text.lower().strip()!='bye'):
        print('speak (say bye to end)')
        print(listen())

