import numpy as np
import matplotlib.pyplot as plt

plt.ion() # decimos de forma explicita que sea interactivo

y = [] # los datos que vamos a dibujar y a actualizar

# el bucle infinito que ira dibujando
while True:
    y.append(np.random.randn(1)) # anadimos un valor aleatorio a la lista y

    # Estas condiciones las he incluido solo para dibujar los ultimos 
    # 10 datos de la lista y ya que quiero que en el grafico se 
    # vea la evolucion de los ultimos datos
    if len(y) <= 10:
        plt.plot(y)
    else:
        plt.plot(y[-10:])

    plt.pause(0.05) # esto pausara el grafico
    plt.cla() # esto limpia la informacian del axis (el area blanca dondes se pintan las cosas.