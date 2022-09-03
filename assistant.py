import pyttsx3 
import datetime
import pyaudio 
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import smtplib
import psutil
import pyjokes
import pyautogui
import random
import requests
from pprint import pprint



MASTER = "Derek"
print("Initializing Hobbs...")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak('The current time is')
    speak(Time)



def wishme():
   speak("Welcome back Mister Streidl!")
   #speak("the current time is")
   time()
   #speak("it's the")
   
   hour = datetime.datetime.now().hour
   if hour >= 0 and hour<12:
       speak("Good Morning" + MASTER)
   elif hour >=12 and hour<18:
        speak("Good Afternoon" + MASTER)
   elif hour >=18 and hour <24:
        speak("Good evening" + MASTER)
   else:
        speak("Good Night" + MASTER)
   speak("Hobbs at your service, how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return  "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('strdere@gmail.com', 'Strdere309')
    server.sendmail("sender@gmail.com", to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    """battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)"""

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/strdere/OneDrive/pictures/screenshots.png')

def who_am_i():
     speak('You are ' + MASTER + ', an okay guy, but you need to impprove.')
     
def where_born():
    speak('I was created by a wizard named Derek, but I was born in New Jersey.')

def how_are_you():
    speak('Could be better, shit. How can help bro?')




if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()

        
        elif 'who am i' in query:
            who_am_i()
        
        elif 'where were you born' in query:
            where_born()
        
        elif 'how are you' in query:
            how_are_you()

        elif 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak('According to Wikipedia...')
            print(results)
            speak(results)
        
        elif 'send email' in query.lower():
            try:
                speak('What should I send...')
                content = takeCommand()
                speak('Who is the Receiver Sir?')
                receiver = input("Enter Receiver's Email :")
                to = receiver
                sendEmail(to, content)
                speak('Email sent Successfuly')

            except Exception as e:
                print(e)
                speak('Unable to send Email')
        
        elif 'search in chrome' in query.lower():
            speak('What should I Search?')
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takeCommand().lower()
            webbrowser.get(chrome_path).open_new_tab(search+'.com')
        
        elif 'search youtube' in query:
            speak('What should I Search?')
            search_term = takeCommand().lower()
            speak("Opening YOUTUBE!")
            webbrowser.open('https://www.youtube.com/results?search_query='+search_term)
        
        elif 'weather details' in query: #weathermap Api
            speak('Which City Sir!')
            weather_up = takeCommand().lower()
            speak('Getting Weather Update for '+ weather_up)
            url = 'http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json'.format(weather_up)
            
            resi = requests.get(url)
            data = resi.json()
            temp = data['main']['temp'],
            wind_speed = data['wind']['speed'],
            latitude = data['coord']['lat'],
            longitude = data['coord']['lon'],
            description = data['weather'][0]['description']

            speak('Temperature is at: {} degree farenheight'.format(temp))
            speak('Wind Speed is at: {} Micro Seconds'.format(wind_speed))
            speak('Latitude is : {}'.format(latitude))
            speak('Longitude is : {}'.format(longitude))
            speak('Clouds Status are : {}'.format(description))
            #update = webbrowser.open('https://api.openweathermap.org/data/2.5/weather?q={}&appid={API KEY}'.format(weather_up))

        elif 'open google' in query:
            speak('What should I Search?')
            search_term = takeCommand().lower()
            speak('Searching...')
            url = 'google.com'
            chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
            webbrowser.open('https://www.google.com/search?q='+search_term)
        
        elif 'open github' in query:
            speak('Opening Github Sir!')
            search_term = takeCommand().lower()
            speak('Opening your Account Sir!')
            url = 'github.com'
            webbrowser.open('https://www.github.com/Derek-Strides')
        
        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            joke()
        
        elif 'go offline' in query:
            speak('Going Offline Sir!')
            quit()
        
        elif 'open word' in query:
            speak('Opening MS Word....')
            ms_word = r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office/WINWORD.EXE'
            os.startfile(ms_word)
        
        elif 'open downloads' in query:
            speak('Opening Downloads....')
            downloads = r'C:/Users/Tech/Downloads'
            os.startfile(downloads)
        
        
        elif 'write a note' in query:
            speak("What Should i write, Sir?")
            notes = takeCommand()
            file = open('notes.txt','w')
            speak("Sir Should I include Date and Time?")
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done taking Notes, Sir!")
            else:
                file.write(notes)
        
        elif 'show notes' in query:
            speak('Showing Notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()
        
        elif 'play music' in query:
            songs_dir = 'E:/Bongo'
            music = os.listdir(songs_dir)
            speak('What should I play?')
            speak('Select a number......')
            answer = takeCommand().lower()
            while('number' not in answer and answer != 'random' and answer != 'you choose'):
                speak('I could not understand you. Please attempt once more')
                answer = takeCommand().lower()
            if 'number' in answer:
                no = int(answer.replace('number',''))
            elif 'random' or 'you choose' in answer:
                no  = random.randint(1,100)
            os.startfile(os.path.join(songs_dir,music[no]))
        
        elif 'who are you' in query:
            speak("I am Hobbs, old man and Mac fanatic, i am addicted to apple.")

