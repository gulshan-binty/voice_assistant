import json
import random
import pyttsx3
import speech_recognition as sr
from difflib import get_close_matches

listener=sr.Recognizer()
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)


with open('intents.json') as file:
    intents = json.load(file)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognition
recognizer = sr.Recognizer()

# Function to get a random response from the intent's responses list
def get_random_response(intent):
    return random.choice(intent['responses'])

# Function to handle user input and generate a response
def process_input(user_input):
    user_input = user_input.lower()

    # Check for each intent
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if user_input == pattern.lower():
                return get_random_response(intent)
            elif user_input.startswith('google:'):
                return get_random_response(intents['intents'][0])  # Redirect to Google
            elif user_input.startswith('greeting:'):
                return get_random_response(intents['intents'][1])
            elif user_input.startswith('goodbye:'):
                return get_random_response(intents['intents'][2])
            elif user_input.startswith('thanks:'):
                return get_random_response(intents['intents'][3])
            elif user_input.startswith('noanswer:'):
                return get_random_response(intents['intents'][4])
            elif user_input.startswith('options:') or 'help' in user_input:
                return get_random_response(intents['intents'][5])  # Fetch weather information
            elif user_input.startswith('news') or 'latest news' in user_input:
                return get_random_response(intents['intents'][18])  # Fetch news information
            elif user_input.startswith('jokes:'):
                return get_random_response(intents['intents'][6])  # Fetch top songs information
            elif user_input.startswith('Identity:'):
                return get_random_response(intents['intents'][7])  # Set a timer
            elif user_input.startswith('datetime:'):
                return get_random_response(intents['intents'][8])  # Fetch COVID-19 information
            elif user_input.startswith('whatsup:'):
                return get_random_response(intents['intents'][9])
            elif user_input.startswith('haha:'):
                return get_random_response(intents['intents'][10])
            elif user_input.startswith('programmer:'):
                return get_random_response(intents['intents'][11])
            elif user_input.startswith('insult:'):
                return get_random_response(intents['intents'][12])
            elif user_input.startswith('activity:'):
                return get_random_response(intents['intents'][13])
            elif user_input.startswith('exclaim:'):
                return get_random_response(intents['intents'][14])
            elif user_input.startswith('weather:'):
                return get_random_response(intents['intents'][15])
            elif user_input.startswith('karan:'):
                return get_random_response(intents['intents'][16])
            elif user_input.startswith('contact:'):
                return get_random_response(intents['intents'][17])
            elif user_input.startswith('appreciate:'):
                return get_random_response(intents['intents'][18])
            elif user_input.startswith('nicetty:'):
                return get_random_response(intents['intents'][19])
            elif user_input.startswith('no:'):
                return get_random_response(intents['intents'][20])
            elif user_input.startswith('news:'):
                return get_random_response(intents['intents'][21])
            elif user_input.startswith('inspire:'):
                return get_random_response(intents['intents'][22])
            elif user_input.startswith('cricket:'):
                return get_random_response(intents['intents'][23])
            elif user_input.startswith('song:'):
                return get_random_response(intents['intents'][24])
            elif user_input.startswith('greetreply:'):
                return get_random_response(intents['intents'][25])
            elif user_input.startswith('riddle:'):
                return get_random_response(intents['intents'][29])
            elif user_input.startswith('age:'):
                return get_random_response(intents['intents'][30])
            elif user_input.startswith('suggest') or 'suggestions' in user_input:
                return get_random_response(intents['intents'][26])  # Suggest improvements

    return get_random_response(intents['intents'][4])  # Default response for no match

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("User input:", user_input)
        return user_input
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't reach the speech recognition service.")
        return ""

# Main program loop
while True:
    # Listen to user input
    user_input = listen()

    # Process user input and get a response
    response = process_input(user_input)

    # Speak the response
    speak(response)
