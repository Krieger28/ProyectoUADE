import time
import os
import random



clear = lambda: os.system('cls')



# Funcion para generar un tablero

alto = 20
ancho = 10

def imprimirTablero(tablero):
    print("+" + "--" * ancho + "+") # Borde de arriba

    for fila in tablero:
        print("|" + "".join(fila) + "|")  # Filas del tablero

    print("+" + "--" * ancho + "+") # Borde de abajo

def crearTablero():
    return [[ "⬛" for _ in range(ancho)] for _ in range(alto)]


# Funcion para 

def crearFPS (tablero):
    
    i=0 
    j=0
    while i < 2234556: # if booolean == False: dsp reemplazar con  esto y vincularlo 
        #con un input del teclado esc o algo asi
        
        time.sleep(0.3)
        clear()
        imprimirTablero(tablero) 
    
# Funcion para crear piezas con sus formas

# Funcion para que seleccione una pieza aleatoria

# Funcion para que se coloque la pieza en el tablero

# Funcion para la actualizacion de la terminal a 1 fps

# Funcion para que se detecte los inputs del usuario

# Funcion para rotar piezas 

# Funcion para detectar si una celda del tablero esta ocupada

# Funcion para simular la caida de la pieza manual y automaticamente

# Funcion para que detecte en el tablero si una fila esta completa

#  Funcion para que si una pieza no puede ingresar al tablero por 
# estar lleno de por finalizado el juego



# function para hacer funcionar las funciones
def main():
    tablero = crearTablero()
    crearFPS (tablero)
main()
