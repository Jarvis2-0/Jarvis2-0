import pyttsx3
import speech_recognition as sr
import time
import datetime
from datetime import date,timedelta
import wikipedia
import webbrowser
import os
import requests
from requests import get
import pywhatkit as kit
import smtplib
import psutil
import pyautogui
import playsound
from PyDictionary import PyDictionary as dicti
from pywikihow import search_wikihow 
import time
from PIL import Image
import newsapi
import pyjokes
import subprocess, sys

#-----------------Memory-----------#
user = "Akshay"
Greetings = ["hello Jessi", "wake up Jessi", "hey Jessi", "get back to work Jessi", "Jessi are you there", "time to work", "ok Jessi" "come online Jessi"]
Greetings_res = ["always there for you sir", "i am ready sir", "always there for you", "how may i help you sir", "i am online and fully ready sir", "your wish my command"]


calendar_strs = ["Todays schedule", "do i have plans", "tell me todays plans", "report my schedule", "am i busy" ]

#-----------------------------------#

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',250)


def speak(audio): 
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def startup() :
    # speak("Initializing Jessi...")
    # speak("Starting all systems applications...")
    # speak("Installing and checking all drivers...")
    # speak("Caliberating and examining all the core processors...")
    # speak("Checking the internet connection...")
    # speak("Wait a moment sir...")
    # speak("All drivers are up and running...")
    # speak("All systems have been activated...")
    # speak("Now I am online...")
    
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning sir")
    elif hour>12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    c_time = time.strftime("%I:%M %p")
    speak(f"currently it is {c_time},lets do some work!!! How may i assist you?" )
     
# def wishme():
    # hour = int(datetime.datetime.now().hour)
    # if hour>=0 and hour<12:
    #     speak('Good Morning!')
    # elif hour>=12 and hour<18:
    #     speak('Good Afternoon!')
    # else:
    #     speak('Good Evening!')
    # speak('I am Jessi 2.0, How may i assist you?')

# def usrname():
#     speak("What should i call you?")
#     uname = takecommand()
#     speak("Welcome Mister"  + uname)
#     speak("How can i Assist you?")

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
        speak("I could not understand, Please Say that again please...")
        return takecommand()  
    return query
    

def weather():
    speak("which citys weather you want to know sir?")
    city = takecommand().lower()

    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    speak(f"The Temperature of {city} is {format(temp2)} degree Celsius \nAnd the Weather is {format(temp1)}")

# def news():
#     newsapi = NewsApiclient(api_key='5840b303fbf949c9985f0e1016fc1155')
#     speak("What topic you need the news about")
#     topic = takecommand()
#     data = newsapi.get_top_headlines(q=topic, language="en", page_size=5)
#     newsData = data["articles"]
#     for y in newsData:
#         speak(y["description"])

def dict():
    speak("Tell me the problem!")
    prob1 =takecommand().lower()

    if 'meaning' in prob1:
        prob1 = prob1.replace('what is the', "")
        prob1 = prob1.replace('Jessi', "")
        prob1 = prob1.replace("meaning of","")
        result1 = dicti.meaning(prob1)
        speak(f'The Meaning of {prob1} is {result1}')

    speak('Exited Dictonary!!!')

def OpenApps():
        speak('Ok Sir, Wait a moment')      
        if 'open text' in  query or 'open notepad' in query:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/System/Applications/TextEdit.app"]) 
            
        elif 'open terminal' in  query or 'open command' in query:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/System/Applications//Utilities/Terminal.app"]) 
            

        elif 'play music' in  query:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/System/Applications/Resso.app"])   
          

        elif 'open whatsapp' in  query:
          subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/whatsApp.app"])     
       
        
        elif 'open google' in  query:
            speak("sir, what should i search on google") 
            webbrowser.open("https://www.google.com/search?q=" +takecommand())
          
       
        elif 'open notes' in  query:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/System/Applications/Notes.app"])     
        
        

        elif 'click' in  query or 'capture' in query:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/System/Applications/Photo Booth.app"])     

        elif 'phone call' in  query:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/System/Applications/Contacts.app"])     

        elif 'youtube' in query:
            speak("What you want to search on youtube, sir!")
            kit.playonyt(takecommand())
            speak("Enjoy Your Time, sir!")

        elif 'facebook' in query:
            controller = webbrowser.get()
            controller.open("https://www.facebook.com/")

        elif 'instagram' in query:
            controller = webbrowser.get()
            controller.open("https://www.instagram.com/")
    

        elif 'gmail' in query:
            controller = webbrowser.get()
            controller.open("https://accounts.google.com/AccountChooser/identifier?flowName=GlifWebSignIn&flowEntry=AccountChooser")

        elif 'open zoom' in  query:
            subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/System/Applications/zoom.us.app"])     
       
def closeapp():
        speak('Ok Sir closing, Wait a moment')  

        if 'close text' in  query or 'close notepad' in query:
            os.system("pkill TextEdit")
        
        elif 'close terminal' in  query or 'close command' in query:
            os.system("pkill Terminal")

        elif 'stop music' in  query:  
            os.system("pkill Resso")

        elif 'close whatsapp' in  query:  
            os.system("pkill whatsApp")

        elif 'close notes' in  query:  
            os.system("pkill Notes")

        elif 'close photo' in  query or 'close camera' in query:
            os.system("pkill Photo Booth")

        elif 'close contacts' in  query or 'close call' in query:
            os.system("pkill Contacts")
        
        elif 'close facebook' in  query:
            os.system("pkill webbrowser")

        elif 'close google' in  query:  
            os.system("pkill Brave Browser")

        elif 'close youtube' in  query:  
            os.system("pkill YouTube")




if __name__ == "__main__":
    startup()
    # wishme() 
    # usrname()# --->if you want to give your name to Jessi<---
    while True:
    # if 1 : ----> to get query execute only once<----
        query = takecommand().lower()

   #Commands for Jessi
#---> To search on wikipidea<---
        if 'wikipedia' in query:
            speak('Searching on wikipidea....')
            query = query.replace('wikipidea', '')
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipidea')
            speak(results)

#---> To open/close applications<---
        elif 'open text' in  query or 'open notepad' in query:
            OpenApps()

        elif 'open terminal' in  query or 'open command' in query:
            OpenApps()
        
        elif 'play music' in  query:
            OpenApps()

        elif 'open whatsapp' in  query:
            OpenApps()

        elif 'open google' in  query:
            OpenApps()
        
        elif 'open notes' in  query:
            OpenApps()
        
        elif 'click' in  query or 'capture' in query:
            OpenApps()

        elif 'phone call' in  query:
            OpenApps()

        elif 'youtube' in query:
            OpenApps()

        elif 'facebook' in query:
            OpenApps()
        
        elif 'instagram' in query:
            OpenApps()

        elif 'gmail' in query:
            OpenApps()

        elif 'open zoom' in  query:
            OpenApps()

        elif 'close text' in  query or 'close notepad' in query:
            closeapp()
     
        elif 'stop music' in  query:  
           closeapp()

        elif 'close whatsapp' in  query:  
            closeapp()

        elif 'close terminal' in  query:  
            closeapp()

        elif 'close notes' in  query:  
            closeapp()

        elif 'close google' in  query:  
            closeapp()

        elif 'close youtube' in  query:  
            closeapp()

        elif 'close photo' in  query or 'close camera' in query:
          closeapp()

        elif 'close contacts' in  query or 'close call' in query:
            closeapp()
        
        elif 'close facebook' in  query:
            closeapp()
    
       
        
# Timepass:
        elif 'you need a break' in query: 
            speak("Ok Sir, you Can call me Anytime!!, just say wakeup!!")
            break

        elif 'Jessi pani lao' in query:
            speak("Ye faltu ke kaam main nahi krta kisi or ko bolo...")
#---> to get current time<---
        elif 'time'   in query:
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S %p")
            speak("Sir Current Time is" + current_time)
#---> to get current date<---
        elif ('date' in query):
            speak("Todays date is " + str(datetime.datetime.now().day)
               + " " + str(datetime.datetime.now().month)
               + " " + str(datetime.datetime.now().year))
#---> to get the weather<---
        elif 'weather' in query:
            weather()
# ---> to get the latest news on any topic<---
        
        # elif "news" in query:
        #     news()

        elif 'no' in query or "No" in query:
            speak("Thank you sir! meet you soon!")
            sys.exit()
       
#---> to listen some jokes by pyhton<---        
        elif ("joke" in query):
            speak(pyjokes.get_joke())


        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak(f"Locating {location}, Please wait...")
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        
        elif "don't listen" in query or "stop listening" in query or "take a break" in query or "wait" in query or "sleep" in query :
            speak("for how much time you want to stop me from listening commands")
            a = int(takecommand())
            speak(f"Ok sir.., i am taking a nap for {a} seconds")
            time.sleep(a)
            speak("it was a nice sleep, The time is over sir, i am back to work")
        
        elif "cpu" in query:
            speak(f"Cpu is at {str(psutil.cpu_percent())} %")
        
        elif "ip" in query or "ip address" in query:
            ipad= get("https://api.ipify.org/").text
            speak("Your IP Address is:"+ipad) 
         
        elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
                speak("By what name do you want to save the screenshot?")
                name = takecommand().lower()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

        elif "show me the screenshot" in query:
                try:
                    speak("Which screen shot do you want to see?")
                    name = takecommand()
                    img = Image.open(f'/Users/akkipatil/Desktop/Desktop/Project/JAIVA/{name}.png')
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)
                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")   

        elif "close screenshot" in query:
            os.system("pkill Preview")
    
        elif 'find' in query or 'dictionary' in query:
            dict()
       
        elif 'alarm' in query:
            speak("Enter the time....")
            time = input(": Enter the time :")

            while True:
                Time = datetime.datetime.now()
                now = Time.strftime("%I:%M %p")

                if now == time:
                    speak('Time to wakeup sir...!')
                    playsound.playsound("test.mp3")
                    
                elif now>time:
                    speak("Alarm closed!")
                    break
        
        elif 'remember that' in query:
            rememberMsg =   query.replace("remember that", "")
            speak("You Tell me  to Remind  You that :"+rememberMsg)
            remember = open('data.txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt', 'r')
            speak("You tell me to remember this:"+remember.read()) 
    
        elif 'my location' in query:
            speak('You are Here:')
            controller = webbrowser.get()
            controller.open("https://www.google.com/maps/place/Latur,+Maharashtra/@18.3936213,76.5458762,12.56z/data=!4m6!3m5!1s0x3bcf83bd7132cd29:0x83629bac5848da3e!8m2!3d18.4087934!4d76.5603828!16s%2Fm%2F05zx_k2")



        # elif ' how' in query or 'what is' in query or 'who' in query :
        #     speak("Let me check.....wait a mmoment... ")
        #     max_result = 1
        #     how_to_func = search_wikihow(max_result)
        #     assert len(how_to_func) == 1
        #     how_to_func[0].print()
        #     speak(how_to_func[0].summry)
           
          
       
       
        elif 'who are you' in  query or 'tell me about yourself' in query:
            
            speak('My Name is Jessi, A Virtual Assistant, Mr. Akshay Created me in python for performing some tasks by voice, I can do tasks like Opening Google, Play music, Open Youtube,  Can tell current time, Oepening notes and texteditor for you,and also Open applications like whatsapp, Music app etc, i can search wikipidea for any information u ask for. ')
       
        elif 'thank you' in  query :
             speak('Welcome sir! , if you need help, Call me anytime')
             quit()
      






        elif 'stop' in  query or 'quit' in  query or 'exit' in  query or 'offline' in  query or 'bye' in  query:
            hour = datetime.datetime.now().hour
            if  (hour >= 18) and (hour < 24):
              speak(f"Okay {user} Sir! Good Night, Have a nice sleep!")
            else:
              speak(f"Okay {user} sir! Have a nice day! ")
              quit()
            sys.exit()
        speak("Do you have any other work to do?")
