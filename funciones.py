import csv
import numpy as np
import matplotlib.pyplot as plt
import time

ahora = time.strftime("%c")
nombre_archivo = ahora+'.csv'

plt.ion() # decimos de forma explicita que sea interactivo
# los datos que vamos a dibujar y a actualizar
af3 = []
t7 = []
pz = []
t8 = []
af4 = []

rango = 30

convulsion = False
contador = 0
bandera = 0

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
    pz.append(data[2])
    t8.append(data[3])
    af4.append(data[4])

    # Estas condiciones las he incluido solo para dibujar los ultimos 
    # 10 datos de la lista y ya que quiero que en el grafico se 
    # vea la evolucion de los ultimos datos
    if len(af3) <= rango:        
        plt.plot(af3,'-',linewidth=2,color='g')
        plt.plot(t7,'-',linewidth=2,color='r')
        plt.plot(pz,'-',linewidth=2,color='b')
        plt.plot(t8,'-',linewidth=2,color='c')
        plt.plot(af4,'-',linewidth=2,color='m')
    else:        
        plt.plot(af3[-rango:],'-',linewidth=2,color='g')
        plt.plot(t7[-rango:],'-',linewidth=2,color='r')
        plt.plot(pz[-rango:],'-',linewidth=2,color='b')
        plt.plot(t8[-rango:],'-',linewidth=2,color='c')
        plt.plot(af4[-rango:],'-',linewidth=2,color='m')

    plt.xlabel('Rango')
    plt.ylabel('Amplitud')
    plt.title('Grafica Convulsion')
    plt.pause(0.05) # esto pausara el grafico
    plt.cla() # esto limpia la informacian del axis (el area blanca dondes se pintan las cosas.

def analisis(data, umbral, lapso, tiempo_lectura):
    global convulsion, contador
    auxiliar = 1/tiempo_lectura # calcula el numero de iteraciones deberia calcular en 1 segundo
    lapso_total = lapso * auxiliar

    try:
        af3 = float(data[0])
        t7 = float(data[1])
        pz = float(data[2])
        t8 = float(data[3])
        af4 = float(data[4])

        # si alguno de los valores obtenidos supera al limite establecido (umbral)        
        if ((af3>umbral) or (t7>umbral) or (pz>umbral) or (t8>umbral) or (af4>umbral)):
            # y si ademas, el tiempo es igual o supera al establecido (tiempo -> en segundos)
            contador += auxiliar # guarda el ultivo valor            
    except:
        print("No se pudo procesar toda la informacion")
    
    if (contador>=lapso_total): # si las iteraciones sobrepasan el tiempo de referencia (lapso) establecido
        convulsion = True # paciente convulsionando
    
    if (convulsion): # si es verdadero
        print ('El paciente esta convulsionando')
        grafica(data) # grafica los valores
    else: # caso contrario (es decir, es falso)
        print ('El paciente no esta convulsionando')

    exportar_csv(data, nombre_archivo); # exporta los datos al archivo csv