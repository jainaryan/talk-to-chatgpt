import openai

import pyttsx3
import speech_recognition as sr

def getUserInput():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    mic = sr.Microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("what is your query: ")
        print("what is your query: \n ")
        audio = r.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return str(text)
        except sr.UnknownValueError:
            print("repeat again please \n")
        except sr.RequestError:
            print("speech service down \n")

def getOutput():
    query = getUserInput()
    #enter your API Key
    API_KEY = 'XXXX'
    openai.api_key = API_KEY
    #text model
    model = 'text-davinci-003'
    result = openai.Completion.create(
        prompt = query,
        model = model,
        max_tokens = 700,
        temperature = 0.85,
        n = 1
    )
    for i in result.choices:
        language = 'en'
        print(i.text)
        pyttsx3.speak(i.text)

getOutput()