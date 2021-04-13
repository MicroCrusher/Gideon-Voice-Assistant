# wolframalpha app id = VJYX5T-V6VK8H6XXV
import speech_recognition as sr
from gtts import gTTS
import os
import uuid
import random
import wolframalpha
client = wolframalpha.Client('VJYX5T-98TAGYEGYH')
import wikipedia
import time
import requests

# GUi_demo

import PySimpleGUI as sg
sg.theme('DarkBlue11')

#text to speech
import playsound
import speech_recognition as sr
from gtts import gTTS
import random
import os

r1 = random.randint(1,10000000)
r2 = random.randint(1,10000000)

randfile = str(r2)+"randomtext"+str(r1) +".mp3"
def speak(text):
    tts=gTTS(text=text, lang="en")
   # filename="voice.mp3"
    tts.save(randfile)
    playsound.playsound(randfile)
    os.remove(randfile)
   # speak(text)

def speak2(text):
    tts=gTTS(text=text, lang="en")
    #filename="voice.mp3"
    playsound.playsound(randfile)

#FUNCTION THAT RETURNS VOICE
def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""

        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said


# Window layout

layout = [[sg.Text("Enter a Command"), sg.InputText()],
 #         [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the window
window = sg.Window('Welcome to GIDEON.', layout) #,size=(200, 300))

#speak("Hello, I am Gideon, your personal assistant. How can I help you today")


# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    
    # See if user wants to quit or window was closed
    if event in(None, 'Cancel.'):
        
        break
    
    # Output a message to the window
 #   window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! I am GIDEON, your virtual assistant")

    res = client.query(values[0])
    wolfram_res = next(res.results).text
    wiki_res = wikipedia.summary(values[0], sentences=2)
    #
    speak(wolfram_res)
    sg.PopupNonBlocking(wolfram_res)
    
#    engine.runAndWait()
# Finish up by removing from the screen
window.close()

# end window sample
