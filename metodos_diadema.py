import json
import ssl
import time
from websocket import create_connection
class Cortex():
	def __init__(self,user):
		self.ws = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})
		self.user=user

	def requestAccess(self):
		request= {
    		"id": 1,
    		"jsonrpc": "2.0",
    		"method": "requestAccess",
    		"params": {
        		"clientId": self.user['client_id'],
        		"clientSecret": self.user['client_secret']
    		}
		}
		self.ws.send(json.dumps(request))
		result = json.loads(self.ws.recv())
		print(json.dumps(result, indent=4))

	def authorize(self):
		request={
    		"id": 1,
    		"jsonrpc": "2.0",
    		"method": "authorize",
    		"params": {
        		"clientId": self.user['client_id'],
        		"clientSecret": self.user['client_secret'],
        		"debit": self.user['debit']
    		}
		}
		self.ws.send(json.dumps(request))
		result = json.loads(self.ws.recv())
		print(json.dumps(result, indent=4))
		self.user['token']=result['result']['cortexToken']
		

	def generateNewToken(self,token):
		request={
    		"id": 1,
    		"jsonrpc": "2.0",
    		"method": "generateNewToken",
    		"params": {
    			"cortexToken": token,
        		"clientId": self.user['client_id'],
        		"clientSecret": self.user['client_secret']
    		}
		}
		self.ws.send(json.dumps(request))
		result = json.loads(self.ws.recv())
		print(json.dumps(result, indent=4))

	def queryHeadsets(self):
		request={
    		"id": 1,
    		"jsonrpc": "2.0",
    		"method": "queryHeadsets",
		}
		self.ws.send(json.dumps(request))

		result = json.loads(self.ws.recv())
		print(json.dumps(result, indent=4))

	def createSession(self):
		request={
    		"id": 1,
    		"jsonrpc": "2.0",
    		"method": "createSession",
    		"params": {
        		"cortexToken": self.user['token'],
        		"headset": self.user['headset'],
        		"status": "active"
    		}
		}
		self.ws.send(json.dumps(request))
		result = json.loads(self.ws.recv())
		print(json.dumps(result, indent=4))
		self.user['sessionId'] = result['result']['id']
		
	def subscribe(self):
		request={
    		"id": 1,
    		"jsonrpc": "2.0",
    		"method": "subscribe",
    		"params": {
       			"cortexToken": self.user['token'],
        		"session": self.user['sessionId'],
        		"streams": ["eeg"]
    		}
		}
		self.ws.send(json.dumps(request))
		result = json.loads(self.ws.recv())
		print(json.dumps(result, indent=4))
		time.sleep(3)

	def unsubscribe(self):
		request={
    		"id": 1,
    		"jsonrpc": "2.0",
    		"method": "unsubscribe",
    		"params": {
       			"cortexToken": self.user['token'],
        		"session": self.user['sessionId'],
        		"streams": ["eeg"]
    		}
		}
		self.ws.send(json.dumps(request))
		result = json.loads(self.ws.recv())
		self.datosraw=result['eeg'][2:7]
		
		#print(json.dumps(result, indent=4))
		# for i in range(10):
		# 	self.ws.send(json.dumps(request))
		# 	result = json.loads(self.ws.recv())
		# 	datosraw=result['eeg'][2:7]
		# 	print(datosraw)
		# 	time.sleep(0.5)





