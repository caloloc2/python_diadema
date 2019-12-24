import random
import time
from funciones import exportar_csv, grafica

nombre_archivo = 'exportacion.csv'
tiempo_lectura = 0.2

try:    
    while True:
        datos =[random.randint(1000,2500), random.randint(6000,8000), random.randint(4000,4500), random.randint(3000, 3500) ,random.randint(3000, 4000)]
        print(datos)
        time.sleep(tiempo_lectura)

        exportar_csv(datos, nombre_archivo); # exporta los datos al archivo csv
        grafica(datos)
except KeyboardInterrupt:
    print("Exit")