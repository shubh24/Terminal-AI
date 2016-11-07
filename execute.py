import os 
from speak import *
import webbrowser
import requests 
import json
import subprocess

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

def ReminderWithin(task, duration_val, duration_unit):

	if duration_unit == "day":
		duration_unit = "days"
	elif duration_unit == "h":
		duration_unit = "hours"
	elif duration_unit == "min":
		duration_unit = "minutes"
	
	cmd = "echo \'notify-send --urgency=critical \"Remider!\" %s\' | at now + %d %s"%(task, duration_val, duration_unit)
	os.system(cmd)

def ReminderSpecific(task, time, date):

	hour = int(time[:2])
	minute = time[3:5]

	if hour <= 12:
		am_pm = "AM"
	else:
		hour -= 12
		am_pm = "PM"

	time = "%d:%s %s"%(hour, minute, am_pm)

	if date != "":
		
		date_list = date.split("-")
		date = "%s/%s/%s"%(date_list[1], date_list[2], date_list[0])
		print time, date
		cmd = "echo \'notify-send --urgency=critical \"Remider!\" %s\' | at %s %s"%(task, time, date)
	
	else:
		cmd = "echo \'notify-send --urgency=critical \"Remider!\" %s\' | at %s"%(task, time)		
	
	os.system(cmd)


