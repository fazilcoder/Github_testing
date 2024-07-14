import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5') 
# use for the initialization windows voice
voices=engine.getProperty('voices')
 # it tells that there is two inbult voices
# print(voices[0].id) 
engine.setProperty('voice',voices[1].id) # it tells that we are using male voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# this code block describes about the time and wishing about the function

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    elif hour>18 and hour <20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am a jarvis AI Please tell me how i help you ")

def takeCommand():
    #It takes microphone as a input and returns a string as a output
    '''
    It takes microphone as a input and returns a string as a output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('...Listening')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query= r.recognize_google(audio)
        print("user said :",query)
        return query

    except Exception as e:
        print(e)
        print("Say that again please...")
if __name__=="__main__":
    # speak("fazil is agood boy")
    wishme()
    while True:
        query=takeCommand()
        
        # using the query we will conevrt it into the tasks
        if 'Wikipedia' in query:
            speak("searching for wikipedia in query")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query)
            speak("According to wikipedia ")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google ' in query:
            webbrowser.open('google.com')
        
        elif 'open stackoverflow'in query:
            webbrowser.open('stackoverflow.com')

        elif 'open music' in query:
            video_dir="C:\\Users\\fazil\\Videos"
            video=os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir,video[2]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir ,the time is {strTime}")
        
