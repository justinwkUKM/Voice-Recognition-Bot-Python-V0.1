import speech_recognition as sr 
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            alexis_speak(voice_data)
        except sr.UnknownValueError:
            alexis_speak('Sorry I didn\'t get you')
        except sr.RequestError:
            alexis_speak('Sorry my speech service is down')
        return voice_data

def respond(voic_data):
    if 'what is your name' in voic_data.lower():
        alexis_speak('My name is Alexis')
    if 'what time is it' in voic_data.lower():
        alexis_speak(f'Its {ctime()}')
    if 'search' in voic_data.lower():
        search = record_audio('What would you like to search for?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for'+ voic_data)
    if 'find location' in voic_data.lower():
            location = record_audio('What location would you like locate?')
            url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            alexis_speak('Here is what I found for'+voic_data)
    if 'exit' in voic_data:
        exit()

def alexis_speak(audio_string):
    if 'exit' in audio_string:
        tts = gTTS(text='Okay Bye', lang='en')
    else:    
        tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


alexis_speak('Hi! How can I help you?')
while True:
    voic_data = record_audio()
    respond(voic_data)



