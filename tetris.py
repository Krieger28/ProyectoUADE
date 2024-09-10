import keyboard
import time
import os
import random



clear = lambda: os.system('cls')
pieza = "🟨"


# Funcion para generar un tablero

alto = 24
ancho = 10

def imprimirTablero(tablero):
    '''ESCRIBIR LA DESCRIPCION DE CADA FUNCION EN ESTE LUGAR DE CADA FUNCION CON ESTAS COMILLAS'''
    print("+" + "--" * ancho + "+") # Borde de arriba

    for fila in tablero:
        print("|" + "".join(fila) + "|")  # Filas del tablero

    print("+" + "--" * ancho + "+") # Borde de abajo
    
def crearTablero():
    return [[ "⬛" for _ in range(ancho)] for _ in range(alto)]


# Funcion para renderear los cambios en la matriz

def crearFPS (tablero):
    while True:  #  vincularlo  con un input del teclado esc o algo asi y el game over
        
        x, y = ancho // 2, 0
        while True:
            # obtenerPosicionInicial()
            x, y = inputsTeclado(tablero,pieza, x, y)
            time.sleep(0.1)
            
            clear()
            imprimirTablero(tablero)
            nuevo_x, nuevo_y = moverPiezaAbajo(tablero, pieza, x, y)
            if nuevo_y == alto - 1 or (nuevo_y + 1 < alto and tablero[nuevo_y + 1][nuevo_x] != "⬛"):
                break
            
            x, y = nuevo_x, nuevo_y

# Función para obtener una posición inicial aleatoria para una nueva pieza

def obtenerPosicionInicial():
    return (5, 0)

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

def inputsTeclado(tablero, pieza, x, y):
    if keyboard.is_pressed("space") == True:
        pass #bajar mas rapido o insta ponerla en donde quedaria
    if keyboard.is_pressed("down") == True:
        pass #bajar mas rapido o insta ponerla en donde quedaria
    if keyboard.is_pressed("up") == True:
        pass #girar pieza
    if keyboard.is_pressed("left") == True:
        x, y = moverIzq(tablero, pieza, x, y) 
        return x, y
    if keyboard.is_pressed("right") == True:
        x, y = moverDer(tablero, pieza, x, y) 
        return x, y
    if keyboard.is_pressed("esc") == True:
        pass #cerrar juego, ver de aplicarlo al primer  while???
    if keyboard.is_pressed("p") == True:
        pass #Pausar, ver de aplicarlo al primer  while???
    return x, y
    
# Funcion para mover  la pieza a la izquierda

def moverIzq(tablero, pieza, x, y):
    if x - 1 >= 0 and tablero[y][x - 1] == "⬛":
        borrarPieza(tablero, x, y)
        x -= 1
        colocarPieza(tablero, pieza, x, y)
    return x, y 


# Funcion para mover  la pieza a la derecha

def moverDer(tablero, pieza, x, y):
    if x + 1 <= 9 and tablero[y][x + 1] == "⬛":
        borrarPieza(tablero, x, y)
        x += 1
        colocarPieza(tablero, pieza, x, y)
    return x, y 

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




# Funcion para LOG IN



# Funcion para que se detecte los inputs del usuario



# Funcion para que si una pieza no puede ingresar al tablero por estar lleno de por finalizado el juego

# Aumentar velocidad del juego

# Esconder primeras 4 lineas

#

# Input para voler a jugar






# Funcion para que detecte en el tablero si una fila esta completa

#  Funcion para que si una pieza no puede ingresar al tablero por
# estar lleno de por finalizado el juego



# function para hacer funcionar el proyecto
def main():
    tablero = crearTablero()
    crearFPS (tablero)
main()
