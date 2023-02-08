import openai
# import time
import pyttsx3
import speech_recognition as sr

#from gtts import gTTS
#import os
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
mic = sr.Microphone


def getUserInput():
    #with sr.Recognizer as recognizer:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("what is your query: ")
        print("what is your query: \n ")
        audio = r.listen(source)
        #recognizer.adjust_for_ambient_noise(recognizer)

        try:
            text = recognizer.recognize_google(audio)
            return str(text)
        except sr.UnknownValueError:
            print("repeat again please \n")
        except sr.RequestError:
            print("speech service down \n")



query = getUserInput()
#enter your API Key
API_KEY = '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'
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
    #output = gTTS(text=i.text, lang=language, slow = False)
    #output.save("output.mp3")
    #os.system("start output.mp3")
    print(i.text)
    pyttsx3.speak(i.text)


