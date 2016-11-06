import os 
from speak import *
import webbrowser
import requests 
import json

def OpenWebsite(website):

	speak("Opening " + website)
	webbrowser.open_new_tab("https://www." + website)

def GetWeather(city):

	url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=65458039096676ffbdea541d1bf495ef"%(city)
	r = requests.get(url)
	r = r.json()

	scene = r["weather"][0]["description"]
	temp = r["main"]["temp"] - 273
	min_temp = r["main"]["temp_min"] - 273
	max_temp = r["main"]["temp_max"] - 273
	humidity = r["main"]["humidity"]

	response = "Weather in %s. %s, the current temperature is %d degree celsius. The humidity stands at %d percent. Good day!"%(city, scene, temp, humidity )
	speak(response)

