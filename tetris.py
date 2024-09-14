import keyboard
import time
import os
import random


clear = lambda: os.system('cls')
PIEZA = "🟨"
VACIO = "⬛"
ALTO = 24
ANCHO = 10


def crearTablero():
    '''ESTA FUNCION GENERA UN TABLERO DE 10 COLUMNAS POR 24 FILAS'''
    return [[ VACIO for _ in range(ANCHO)] for _ in range(ALTO)]


def imprimirTablero(tablero):
    '''ESTA FUNCION IMPRIME EL TABLERO GENERADO SIN IMPRIMIR LAS PRIMERAS 4 FILAS'''
    print("+" + "--" * ANCHO + "+") # Borde de arriba

    aux=0
    for fila in tablero:
            if aux>=4: #No imprime las primeras 4 filas
                print("|" + "".join(fila) + "|")  # Filas del tablero
            aux+=1
    
    print("+" + "--" * ANCHO + "+") # Borde de abajo
    

def crearFPS (tablero):
    '''ESTA FUNCION SE ENCARGA DE RENDEREAR LOS CAMBIOS A LA MATRIZ. SE TRATA DE UN BUCLE INFINITO QUE CORRE EL PROGRAMA'''
    while True:  #  vincularlo  con un input del teclado esc o algo asi y el game over
        x, y = ANCHO // 2, 0
        while True:
            x, y = inputsTeclado(tablero,PIEZA, x, y)
            time.sleep(0.05)            
            clear()
            imprimirTablero(tablero)
            nuevo_x, nuevo_y = moverPiezaAbajo(tablero, PIEZA, x, y)
            if puedeAvanzar(nuevo_y,tablero,nuevo_x)==False:
                filaCompleta(tablero)
                break   
            x, y = nuevo_x, nuevo_y


'''ESTA FUNCION DETECTA SI LA PIEZA PUEDE AVANZAR O SI HIZO TOPE'''
puedeAvanzar= lambda nuevo_y,tablero,nuevo_x: False if nuevo_y==ALTO - 1 or (nuevo_y + 1 < ALTO and tablero[nuevo_y + 1][nuevo_x] != VACIO) else True


def eliminarFila(tablero, y):
    '''ESTA FUNCION SE ENCARGA DE ELIMINAR LA FILA INDICADA'''
    del tablero[tablero.index(y)]


def agregarFila(tablero):
    '''ESTA FUNCION AGREGA FILAS EN LA POSICION 0 DE LA MATRIZ'''
    tablero.insert(0,[VACIO for _ in range(ANCHO)])    


def filaCompleta(tablero):
    '''ESTA FUNCION DETECTA SI UNA FILA ESTA COMPLETA, EN CASO DE HABER FILAS COMPLETAS, LAS ELIMINA Y AGREGA FILIAS NUEVAS EN LA PARTE ALTA DEL TABLERO'''
    for y in tablero:
        aux=0
        for x in y:
            if x==PIEZA:
                aux+=1
        if aux==10:
            eliminarFila(tablero,y)
            agregarFila(tablero)


def colocarPieza(tablero, pieza, x, y):
    '''ESTA FUNCION COLOCA PIEZAS EN EL TABLERO'''
    if 0 <= x < ANCHO and 0 <= y < ALTO:
        tablero[y][x] = pieza


def borrarPieza(tablero, x, y):
    '''ESTA FUNCION ELIMINA PIEZAS DE POSICIONES ESPECIFICAS'''
    if 0 <= x < ANCHO and 0 <= y < ALTO:
        tablero[y][x] = VACIO


def inputsTeclado(tablero, pieza, x, y):
    '''ESTA FUNCION PERMITE QUE EL SISTEMA DETECTE LOS IMPUTS DEL USUARIO'''
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


def moverIzq(tablero, pieza, x, y):
    '''ESTA FUNCION MUEVE LA PIEZA HACIA LA IZQUIERDA'''
    if x - 1 >= 0 and tablero[y][x - 1] == VACIO:
        borrarPieza(tablero, x, y)
        x -= 1
        colocarPieza(tablero, pieza, x, y)
    return x, y 


def moverDer(tablero, pieza, x, y):
    '''ESTA FUNCION MUEVE LA PIEZA HACIA LA DERECHA'''
    if x + 1 < ANCHO and tablero[y][x + 1] == VACIO:
        borrarPieza(tablero, x, y)
        x += 1
        colocarPieza(tablero, pieza, x, y)
    return x, y 


def moverPiezaAbajo(tablero, pieza, x, y):
    '''ESTA FUNCION SIMULA LA CAIDA DE UNA PIEZA POR EL TABLERO'''
    if y + 1 < ALTO and tablero[y + 1][x] == VACIO:
        borrarPieza(tablero, x, y)
        y += 1
        colocarPieza(tablero, pieza, x, y)
        return x, y
    return x, y


def logIn ():
    '''Esta función se encarga de generar un sistema de login necesario para continuar al programa principal'''
    pass


def finDelJuego():
    '''Esta función se encarga de finalizar el loop principal del juego una vez que una nueva pieza no pueda
    ingresar en 20 filas inferiores de la matriz. También presenta una opcion para “volver a jugar'''  
    # Input para voler a jugar
    pass


def aumentarVel():
    '''Esta función se encarga de aumentar la velocidad del juego a medida que se eliminen filas'''


def main():
    '''ESTA FUNCION SE ENCARGA DE EJECUTAR EL PROYECTO'''
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

