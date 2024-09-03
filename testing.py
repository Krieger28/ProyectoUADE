import time
import os
import random



clear = lambda: os.system('cls')
ancho = 20
alto = 10


def imprimirTablero(tablero):
    print("+" + "--" * alto + "+") # Borde de arriba

    for fila in tablero:
        print("|" + "".join(fila) + "|")  # Filas del tablero

    print("+" + "--" * alto + "+") # Borde de abajo

def crearTablero():
    return [[ "⬛" for _ in range(alto)] for _ in range(ancho)]






def purpleDown(matrix):
    purpleIcon= "🟪"
    
    matrix[j][random.randint(4,5)] = purpleIcon



tableroDefault= crearTablero()
tablero = crearTablero()
i=0 
j=0
while i < 2234556: # if booolean == False: dsp reemplazar con  esto y vincularlo con un input del teclado
    
    
    if j == 20:
        j=0
        tablero = crearTablero()
    purpleDown(tablero)
    time.sleep(0.3)
    clear()
    imprimirTablero(tablero)
    
    if j < 20:
        j+=1
    
def holla():
    pass