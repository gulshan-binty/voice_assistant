import speech_recognition as sr
import pyttsx3
import wikipedia as wk

engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

while True:
    mic=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = mic.listen(source)
        mic.adjust_for_ambient_noise(source)

        try:
            print("Recognizing...")
            user_input = mic.recognize_google(audio)
            summery=wk.summary(user_input)
            print(user_input)
            print(summery)
            # engine.say(summery)
            # engine.runAndWait()
            break
        except:
            print("Sorry, I couldn't get it.")

        
