import random
import time
from funciones import analisis
import Tkinter

tiempo_lectura = 0.1 # tiempo de lectura maximo 1 (1 segundo)

# es establece los limites para el analisis de los datos recibidos
umbral = 5800 # si sobrepasa este valor entra en analisis
lapso = 10 # en segundos

try:    
    while True:
        datos =[random.randint(1000,2500), random.randint(6000,7500), random.randint(4000,4500), random.randint(3000, 3500) ,random.randint(3000, 4000)]
        analisis(datos, umbral, lapso, tiempo_lectura)
        time.sleep(tiempo_lectura)

except KeyboardInterrupt:
    print("Exit")