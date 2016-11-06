import os
from speak import *

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

if __name__ == '__main__':
	
	while(1):
		
		message = listen()
		print message

		if message is not None:
		
			api_res = talkToAPI(message)
			# print api_res
			
			if api_res["status"]["code"] == 200:
				speak(api_res["result"]["fulfillment"]["speech"])

