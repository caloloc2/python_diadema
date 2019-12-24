import json
import ssl
import time
import Tkinter
from websocket import create_connection
from metodos_diadema import *
from funciones import analisis

tiempo_lectura = 0.5 # tiempo de lectura maximo 1 (1 segundo)

# es establece los limites para el analisis de los datos recibidos
umbral = 4500 # si sobrepasa este valor entra en analisis
lapso = 10 # en segundos

user = {
	"license" : "3c0a6486-63d8-4570-b9fd-85551bc81c4b",
	"client_id" : "JjPt3tGxlrWPAsHXQD0QoE9TwbRk8I3yJiKjVZ0Y",
	"client_secret" : "G097NEB0jwNccZ6b3I9o1ZsdG1xGNwzeFHb3EIUc6AXHfgjdav01wVV4OYG0foKmflcv2RUfjn5Zyu48Pgyw7fJQaf3bGeqeYBAnUawDZ2i7F0UWzkTWzc14cnW25CBk",
	"debit" : 100,
	"headset": "INSIGHT-A1D20009"
}

c=Cortex(user)
c.authorize()
c.createSession()
c.subscribe()

try:
	while True:
		c.unsubscribe()
		#print(c.datosraw)
		analisis(c.datosraw, umbral, lapso, tiempo_lectura)
		time.sleep(tiempo_lectura)
except KeyboardInterrupt:
	c.unsubscribe()
	print("Exit")