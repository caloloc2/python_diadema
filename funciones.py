import csv
import matplotlib.pyplot as plt
import time, serial

nombre_archivo = 'exportacion.csv' # nombre del archivo csv a exportar

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

    plt.xlabel('Rango') # nombre al eje x
    plt.ylabel('Amplitud') # nombre al eje y
    plt.title('Grafica Convulsion') # nombre de la grafica
    plt.pause(0.05) # esto pausara el grafico
    plt.cla() # esto limpia la informacian del axis (el area blanca dondes se pintan las cosas.

def analisis(data, umbral, lapso, tiempo_lectura):

    global convulsion, contador
    auxiliar = 1/tiempo_lectura # calcula el numero de iteraciones deberia calcular en 1 segundo
    lapso_total = lapso * auxiliar # calcula el tiempo total a calcularse

    try:
        af3 = float(data[0])
        t7 = float(data[1])
        pz = float(data[2])
        t8 = float(data[3])
        af4 = float(data[4])

        # si alguno de los valores obtenidos supera al limite establecido (umbral)        
        if ((af3>umbral) or (t7>umbral) or (pz>umbral) or (t8>umbral) or (af4>umbral)):
            # si cumple cualquiera de las condiciones, ademas debe sumar en tiempo            
            contador += auxiliar
    except:
        print("No se pudo procesar toda la informacion")
    
    if (contador>=lapso_total): # si las iteraciones sobrepasan el tiempo de referencia (lapso) establecido
        convulsion = True # paciente convulsionando
    
    if (convulsion): # si es verdadero
        print ('El paciente esta convulsionando')
        envio_serial('a') # envia la letra a por puerto serial
        grafica(data) # grafica los valores
    else: # caso contrario (es decir, es falso)
        print ('El paciente no esta convulsionando')
        envio_serial('b') # envia la letra a por puerto serial

    exportar_csv(data, nombre_archivo); # exporta los datos al archivo csv

# funcion para el envio de datos por puerto serial
def envio_serial(dato):
    global puerto, mensaje

    #obtiene el puerto a manejar desde el campo de la ventana
    puerto_com = "COM3" # cambiar al puerto asignado

    if (puerto_com != ""):
        # Iniciando conexion serial
        arduinoPort = serial.Serial(puerto_com, 9600, timeout=1)
        flagCharacter = dato
        
        # Retardo para establecer la conexion serial
        time.sleep(1.8) 
        arduinoPort.write(flagCharacter)        

        # Cerrando puerto serial
        arduinoPort.close()
    else:
        print("No se ha indicado el puerto a usar.")        