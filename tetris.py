import time
import os
import random



clear = lambda: os.system('cls')



# Funcion para generar un tablero

alto = 24
ancho = 10

def imprimirTablero(tablero):
    print("+" + "--" * ancho + "+") # Borde de arriba

    for fila in tablero:
        print("|" + "".join(fila) + "|")  # Filas del tablero

    print("+" + "--" * ancho + "+") # Borde de abajo

def crearTablero():
    return [[ "⬛" for _ in range(ancho)] for _ in range(alto)]


# Funcion para renderear los cambios en la matriz

def crearFPS (tablero):
    while True:  #  vincularlo  con un input del teclado esc o algo asi y el game over
        pieza = "🟨" 
        x, y = ancho // 2, 0
        while True:
            obtenerPosicionInicial()
            time.sleep(0.3)
            clear()
            imprimirTablero(tablero) 
            nuevo_x, nuevo_y = moverPiezaAbajo(tablero, pieza, x, y)
            if nuevo_y == alto - 1 or (nuevo_y + 1 < alto and tablero[nuevo_y + 1][nuevo_x] != "⬛"):
                break
            x, y = nuevo_x, nuevo_y
    
# Función para obtener una posición inicial aleatoria para una nueva pieza
    
def obtenerPosicionInicial():
    return (random.randint(0, ancho - 1), 0)

# Funcion para crear piezas con sus formas

# Funcion para que seleccione una pieza aleatoria

# Funcion para que se coloque la pieza en el tablero

def colocarPieza(tablero, pieza, x, y):
    if 0 <= x < ancho and 0 <= y < alto:
        tablero[y][x] = pieza

# function para Borrar la pieza de la posicion anterior
def borrarPieza(tablero, x, y):
    if 0 <= x < ancho and 0 <= y < alto:
        tablero[y][x] = "⬛"

# Funcion para que se detecte los inputs del usuario

# Funcion para rotar piezas 

# Funcion para simular la caida de la pieza manual

# Funcion para simular la caida de la pieza automaticamente

def moverPiezaAbajo(tablero, pieza, x, y):
    if y + 1 < alto and tablero[y + 1][x] == "⬛":
        borrarPieza(tablero, x, y)
        y += 1
        colocarPieza(tablero, pieza, x, y)
        return x, y
    return x, y



# Funcion para que detecte en el tablero si una fila esta completa

#  Funcion para que si una pieza no puede ingresar al tablero por 
# estar lleno de por finalizado el juego



# function para hacer funcionar el proyecto
def main():
    tablero = crearTablero()
    crearFPS (tablero)
main()
