import json
import ssl
import time
#from websocket import create_connection
#from metodos_diadema import *
user = {
	"license" : "3c0a6486-63d8-4570-b9fd-85551bc81c4b",
	"client_id" : "JjPt3tGxlrWPAsHXQD0QoE9TwbRk8I3yJiKjVZ0Y",
	"client_secret" : "G097NEB0jwNccZ6b3I9o1ZsdG1xGNwzeFHb3EIUc6AXHfgjdav01wVV4OYG0foKmflcv2RUfjn5Zyu48Pgyw7fJQaf3bGeqeYBAnUawDZ2i7F0UWzkTWzc14cnW25CBk",
	"debit" : 100,
	"headset": "INSIGHT-A1D20009"
}

# c=Cortex(user)
# c.authorize()
# c.createSession()
# c.subscribe()

try:
	while True:
		c.unsubscribe()
		print(c.datosraw)
		time.sleep(0.5)
except KeyboardInterrupt:
	c.unsubscribe()
	print("Exit")