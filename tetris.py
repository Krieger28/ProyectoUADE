import keyboard
import time
import os
import random



clear = lambda: os.system('cls')
PIEZA = "🟨"
VACIO = "⬛"

# Funcion para generar un tablero
ALTO = 24
ANCHO = 10

def imprimirTablero(tablero):
    '''ESCRIBIR LA DESCRIPCION DE CADA FUNCION EN ESTE LUGAR DE CADA FUNCION CON ESTAS COMILLAS'''
    print("+" + "--" * ANCHO + "+") # Borde de arriba

    aux=0
    for fila in tablero:
            if aux>=4: #No imprime las primeras 4 filas
                print("|" + "".join(fila) + "|")  # Filas del tablero
            aux+=1
    
    print("+" + "--" * ANCHO + "+") # Borde de abajo
    
def crearTablero():
    return [[ VACIO for _ in range(ANCHO)] for _ in range(ALTO)]


# Funcion para renderear los cambios en la matriz
def crearFPS (tablero):
    while True:  #  vincularlo  con un input del teclado esc o algo asi y el game over
        x, y = ANCHO // 2, 0
        while True:
            x, y = inputsTeclado(tablero,PIEZA, x, y)
            time.sleep(0.3)            
            clear()
            imprimirTablero(tablero)
            nuevo_x, nuevo_y = moverPiezaAbajo(tablero, PIEZA, x, y)
            if puedeAvanzar(nuevo_y,tablero,nuevo_x)==False:
                break   
            x, y = nuevo_x, nuevo_y


# Funcion para detectar si la pieza hizo tope
puedeAvanzar= lambda nuevo_y,tablero,nuevo_x: False if nuevo_y==ALTO - 1 or (nuevo_y + 1 < ALTO and tablero[nuevo_y + 1][nuevo_x] != VACIO) else True


# Función para obtener una posición inicial para una nueva pieza
def obtenerPosicionInicial():
    return (5, 0)


# Funcion para que se coloque la pieza en el tablero
def colocarPieza(tablero, pieza, x, y):
    if 0 <= x < ANCHO and 0 <= y < ALTO:
        tablero[y][x] = pieza


# function para Borrar la pieza de la posicion anterior
def borrarPieza(tablero, x, y):
    if 0 <= x < ANCHO and 0 <= y < ALTO:
        tablero[y][x] = VACIO


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
        pass #pausar el juego
    return x, y


# Funcion para mover  la pieza a la izquierda
def moverIzq(tablero, pieza, x, y):
    if x - 1 >= 0 and tablero[y][x - 1] == VACIO:
        borrarPieza(tablero, x, y)
        x -= 1
        colocarPieza(tablero, pieza, x, y)
    return x, y 


# Funcion para mover  la pieza a la derecha
def moverDer(tablero, pieza, x, y):
    if x + 1 < ANCHO and tablero[y][x + 1] == VACIO:
        borrarPieza(tablero, x, y)
        x += 1
        colocarPieza(tablero, pieza, x, y)
    return x, y 


# Funcion para simular la caida de la pieza automaticamente
def moverPiezaAbajo(tablero, pieza, x, y):
    if y + 1 < ALTO and tablero[y + 1][x] == VACIO:
        borrarPieza(tablero, x, y)
        y += 1
        colocarPieza(tablero, pieza, x, y)
        return x, y
    return x, y




# Funcion para LOG IN


# Funcion para que si una pieza no puede ingresar al tablero por estar lleno de por finalizado el juego


# Aumentar velocidad del juego


# Input para voler a jugar


# function para hacer funcionar el proyecto
def main():
    tablero = crearTablero()
    crearFPS (tablero)
main()



# Funcion para enviar la pieza al fondo del tablero
# Funcion para crear piezas con sus formas
# Funcion para que seleccione una pieza aleatoria
# Funcion para rotar piezas
# Funcion para que detecte en el tablero si una fila esta completa
# Funcion para eliminar una fila 
# Funcion para agregar una fila

