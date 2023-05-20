import speech_recognition as sr
import os
import subprocess,sys



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e: 
       return "None"
    return query

while True: 
    wake_up =takecommand().lower()
        
    if 'wake up' in wake_up:
        
        path = ("/Users/akkipatil/Desktop/Project/Project/JAIVA/jaiva.py")
       
        assert os.path.exists(path)
        assert os.path.isfile(path)
        with open(path, "r") as path:
            pass


        subprocess.call('/Users/akkipatil/Desktop/Desktop/Project/JAIVA/jaiva.py')
    else:
        print("Restart Again......")
    