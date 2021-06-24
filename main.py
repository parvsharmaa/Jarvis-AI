import pyttsx3
import datetime
import  speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !!")
    else:
        speak("Good Evening !!")

    speak("Hello sir ! I am Jarvis, how may I help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
       print("Recognizing...")
       query = r.recognize_google(audio, language='en-in')
       print("User said:", query)

    except Exception as e:
        # print(e)
        print("Say that again please... :)")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
     query = takeCommand().lower()

     if 'wikipedia' in query:
         speak('Searching wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)

     elif 'open youtube' in query:
         webbrowser.open("youtube.com")

     elif 'open google' in query:
         webbrowser.open("google.com")

     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")

     elif 'play music' in query:
         music_dir = 'D:\\test.music'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))

     elif 'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         print(strTime)
         speak(f"Sir, the present time is {strTime}")

     elif 'open code' in query:
         codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
         os.startfile(codePath)

     elif 'send mail' in query:
         try:
             speak("What should I say sir?")
             content = takeCommand()
             to = "recieveremail@gmail.com"
             sendEmail(to, content)
             speak("Email has been sent")
         except Exception as e:
             print(e)
             speak("something went wrong, Please try again.")

     elif 'close' or 'quit' in query:
         exit()