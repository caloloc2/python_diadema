import csv
import numpy as np
import matplotlib.pyplot as plt

plt.ion() # decimos de forma explicita que sea interactivo
 # los datos que vamos a dibujar y a actualizar
af3 = []
t7 = []
pz = []
t8 = []
af4 = []

rango = 30

def escribir_archivo(data, nombre_archivo, modo):
    myFile = open(nombre_archivo, modo)
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(data)

def exportar_csv(data, nombre_archivo):
    try:
        escribir_archivo(data, nombre_archivo, 'a')
        return True
    except IOError:
        print("No se encuentra el archivo de exportacion... Creando archivo")        
        escribir_archivo(data, nombre_archivo, 'w')
        return False
    # finally:
    #     f.close()

def grafica(data):
    # separamos los valores recibidos
    af3.append(data[0])
    t7.append(data[1])

    # Estas condiciones las he incluido solo para dibujar los ultimos 
    # 10 datos de la lista y ya que quiero que en el grafico se 
    # vea la evolucion de los ultimos datos
    if len(af3) <= rango:        
        plt.plot(af3,'-',linewidth=2,color='g')
        plt.plot(t7,'-',linewidth=2,color='r')
    else:        
        plt.plot(af3[-rango:],'-',linewidth=2,color='g')
        plt.plot(t7[-rango:],'-',linewidth=2,color='r')

    plt.pause(0.05) # esto pausara el grafico
    plt.cla() # esto limpia la informacian del axis (el area blanca dondes se pintan las cosas.