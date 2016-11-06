#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import pyaudio
import speech_recognition as sr
 
from gtts import gTTS
import webbrowser

r = sr.Recognizer()

def listen():

	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)

	try:
		text = r.recognize_google(audio)
		return text

	except:
		return None


def speak(text): 
	
	tts = gTTS(text = text, lang = "en")
	tts.save("voice.mp3")

	webbrowser.open("voice.mp3")
