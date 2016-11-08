import os
from speak import *
import execute

import apiai
import json

CLIENT_ACCESS_TOKEN = '9d100fa2be9b433caa27aa0a424b1e67'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

def talkToAPI(message):

    request = ai.text_request()
    request.lang = 'en' 
    request.query = message
    response = request.getresponse()
    p = response.read()
    res = json.loads(p)
    return res

def parse(api_res):

	if api_res["result"]["source"] == "agent":
	
		intentName = api_res["result"]["metadata"]["intentName"]

		if intentName == "OpenWebsite":
			website = api_res["result"]["fulfillment"]["speech"]
			execute.OpenWebsite(website)
		
		elif intentName == "GetWeather":
			city = api_res["result"]["fulfillment"]["speech"]
			execute.GetWeather(city)

		elif intentName == "ReminderWithin":
			task = api_res["result"]["parameters"]["Task"]
			duration_val = api_res["result"]["parameters"]["duration"]["amount"]
			duration_unit = api_res["result"]["parameters"]["duration"]["unit"]

			execute.ReminderWithin(task, duration_val, duration_unit)

		elif intentName == "ReminderSpecific":
			task = api_res["result"]["parameters"]["Task"]
			date = api_res["result"]["parameters"]["date"]
			time = api_res["result"]["parameters"]["time"]

			execute.ReminderSpecific(task, time, date)

		elif intentName == "ToDo":
			task = api_res["result"]["parameters"]["Task"]
			priority = api_res["result"]["parameters"]["priority"]

			execute.ToDo(task, priority)

		elif intentName == "CheckOff":
			task_index = api_res["result"]["parameters"]["number-integer"]

			execute.CheckOff(task_index)

		elif intentName == "ShowToDo":
			execute.ShowToDo()



	elif api_res["result"]["source"] == "domains":

		speak(api_res["result"]["fulfillment"]["speech"])
	

if __name__ == '__main__':
	
	while(1):
		
		message = listen()
		print message

		if message is not None:
		
			api_res = talkToAPI(message)

			if api_res["status"]["code"] == 200:
				parse(api_res)
			else:
				speak("My intelligence is still a work-in-progress! Can you repeat?")

				
