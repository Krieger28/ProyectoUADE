import keyboard
import time
import os
import random
from re import search

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
O = "🟨"
I = "🟦"
T = "🟪"
L = "🟧"
J = "🟫"
S = "🟥"
Z = "🟩"
VACIO = "⬛"
ALTO = 24
ANCHO = 10

# Definir las piezas con sus rotaciones
PIEZAS = {
    "O": [[[O, O],
           [O, O]]],

    "I": [[[I],
           [I],
           [I],
           [I]],

          [[I, I, I, I]],

        #   [[I],
        #    [I],
        #    [I],
        #    [I]],

        #   [[I, I, I, I]]
        ],

    "T": [[[VACIO, T, VACIO],
           [T, T, T]],

          [[T, VACIO],
           [T, T],
           [T, VACIO]],

          [[T, T, T],
           [VACIO, T, VACIO]],

          [[VACIO, T],
           [T, T],
           [VACIO, T]]],
           
    "L": [[[L, VACIO],
           [L, VACIO],
           [L, L]],

          [[L, L, L],
           [L, VACIO, VACIO]],

          [[L, L],
           [VACIO, L],
           [VACIO, L]],

          [[VACIO, VACIO, L],
           [L, L, L]]],
           
    "J": [[[VACIO, J],
           [VACIO, J],
           [J, J]],

          [[J, VACIO, VACIO],
           [J, J, J]],

          [[J, J],
           [J, VACIO],
           [J, VACIO]],

          [[J, J, J],
           [VACIO, VACIO, J]]],

    "S": [[[VACIO, S, S],
           [S, S, VACIO]],

          [[S, VACIO],
           [S, S],
           [VACIO, S]]],

    "Z": [[[Z, Z, VACIO],
           [VACIO, Z, Z]],

          [[VACIO, Z],
           [Z, Z],
           [Z, VACIO]]]
}

listaPiezas= list(PIEZAS.keys())


def crearTablero():
    return [[VACIO for _ in range(ANCHO)] for _ in range(ALTO)]

def imprimirTablero(tablero):
    print("+" + "--" * ANCHO + "+")
    for i, fila in enumerate(tablero):
        if i >= 0:  # Evita imprimir las primeras 4 filas
            print("|" + "".join(fila) + "|")
    print("+" + "--" * ANCHO + "+")


def crearFPS(tablero):
    pausado = False
    while True:
        pieza, tipo_pieza, color = seleccionarPieza()
        # x, y = ANCHO // 2, 0
        x, y = 4, 0

        if finalizarJuego(tablero):
            break

        while True:
            x, y, pausado, pieza, color = inputsTeclado(tablero, pieza, x, y, pausado, tipo_pieza, color)
            if pausado:
                time.sleep(0.1)
                continue

            # Control de movimiento hacia abajo
            time.sleep(0.05)  # Ajusta la velocidad de caída de la pieza
            clear()
            imprimirTablero(tablero)
            borrarPieza(tablero, pieza, x, y)

            # Verificar si puede avanzar, y mover hacia abajo
            if puedeAvanzar(tablero, pieza, x, y):
                x, y = moverPiezaAbajo(tablero, pieza, x, y, color)
            else:
                colocarPieza(tablero, pieza, x, y, color)
                filaCompleta(tablero)
                break

            colocarPieza(tablero, pieza, x, y, color)


def seleccionarPieza():    
    global listaPiezas
    posicion_aleatoria = random.randint(0, len(listaPiezas)-1) 
    #tipo_pieza = random.choice(piezas)
    tipo_pieza = listaPiezas[posicion_aleatoria] 
    rotaciones = PIEZAS[tipo_pieza]
    rotacion_inicial = rotaciones[0]

    listaPiezas.pop(posicion_aleatoria)
    
    if len(listaPiezas)==0:
        listaPiezas= list(PIEZAS.keys())
    
    if tipo_pieza == "I":
        color = I
    if tipo_pieza == "T":
        color = T
    if tipo_pieza == "L":
        color = L
    if tipo_pieza == "J":
        color = J
    if tipo_pieza == "O":
        color = O
    if tipo_pieza == "S":
        color = S
    if tipo_pieza == "Z":
        color = Z

  
   

    return rotacion_inicial, tipo_pieza, color

def colocarPieza(tablero, pieza, x, y, color):

    for i, fila in enumerate(pieza):
        for j, celda in enumerate(fila):
            if celda != VACIO and 0 <= x + j < ANCHO and 0 <= y + i < ALTO:
            
                tablero[y + i][x + j] = color

def borrarPieza(tablero, pieza, x, y):
    for i, fila in enumerate(pieza):
        for j, celda in enumerate(fila):
            if celda != VACIO and 0 <= x + j < ANCHO and 0 <= y + i < ALTO:
                tablero[y + i][x + j] = VACIO





def rotarPieza(tablero, pieza_actual, tipo_pieza, x, y):

    rotaciones = PIEZAS[tipo_pieza]
    indice_actual = rotaciones.index(pieza_actual)
    pieza_rotada = rotaciones[(indice_actual + 1) % len(rotaciones)]
    
    # esto capas trae el bug de la pieza I que no se acuesta
    ancho_pieza = len(pieza_rotada[0])
    if x + ancho_pieza > ANCHO:
        x = ANCHO - ancho_pieza
    
    # checkea si esta libre la nueva posicion al girarla, con esto adaptandolo capas se arrgla el tema de poner piezas encima de otras cuando vas a la izquierda o derecha
    if all(
        0 <= y + i < ALTO and 0 <= x + j < ANCHO and (tablero[y + i][x + j] == VACIO or pieza_rotada[i][j] == VACIO)
        for i, fila in enumerate(pieza_rotada) for j, celda in enumerate(fila) if celda != VACIO
    ):
        return pieza_rotada, x, y  # Devuelve la nueva rotación y posición ajustada
    else:
        # Si la posición no está libre, no rota la pieza
        return pieza_actual, x, y




def inputsTeclado(tablero, pieza, x, y, pausado, tipo_pieza, color):
    if keyboard.is_pressed("up"):
        borrarPieza(tablero, pieza, x, y)
        pieza, x, y = rotarPieza(tablero, pieza, tipo_pieza, x, y)
        colocarPieza(tablero, pieza, x, y, color)
    if keyboard.is_pressed("left"):
        x, y = moverIzq(tablero, pieza, x, y, color)
    elif keyboard.is_pressed("right"):
        x, y = moverDer(tablero, pieza, x, y, color)
    if keyboard.is_pressed("p"):
        pausado = pausa(pausado)
    return x, y, pausado, pieza, color










#ESTO FUNCIONA PARA GIRAR LAS PIEZAS, EDITANDOLO DE ALGUNA FORMA DEBERIA ANDAR PARA MOVERIZQ Y MOVERDER

# if all(
#         0 <= y + i < ALTO and 0 <= x + j < ANCHO and (tablero[y + i][x + j] == VACIO or pieza_rotada[i][j] == VACIO)
#         for i, fila in enumerate(pieza_rotada) for j, celda in enumerate(fila) if celda != VACIO
#     ):

def moverIzq(tablero, pieza, x, y, color):
    # Verifica si puede mover la pieza hacia la izquierda y la mueve
    if x > 0 and all(
        tablero[y + i][x - 1 + j] == VACIO
        for i, fila in enumerate(pieza)
        for j, celda in enumerate(fila)
        if celda == pieza
        # if celda != VACIO # con esto no choca contra las piezas ya puestras pero solo se mueve la pieza "I"
    ):
        borrarPieza(tablero, pieza, x, y)
        x -= 1
        colocarPieza(tablero, pieza, x, y, color)
    return x, y
# len(pieza)
def moverDer(tablero, pieza, x, y, color):
    # Verifica si puede mover la pieza hacia la derecha y la nueve
    if x + len(pieza[0]) < ANCHO and all(
        tablero[y + i][x + j + 1] == VACIO
        for i, fila in enumerate(pieza)
        for j, celda in enumerate(fila)
        # if celda != VACIO  # con esto no choca contra las piezas ya puestras pero solo se mueve la pieza "I"
        if  celda == pieza
    ):
        borrarPieza(tablero, pieza, x, y)
        x += 1
        colocarPieza(tablero, pieza, x, y, color)
    return x, y 





def moverPiezaAbajo(tablero, pieza, x, y, color):
    # Verifica si hay espacio para mover la pieza hacia abajo
    if y + len(pieza[0]) <= ALTO and all(
        tablero[y + 1 + i][x + j] == VACIO for i, fila in enumerate(pieza) for j, celda in enumerate(fila) if celda != VACIO
    ):
        borrarPieza(tablero, pieza, x, y)
        y += 1
        colocarPieza(tablero, pieza, x, y, color)
    return x, y




def pausa(pausado): 
    pausado = not pausado
    while keyboard.is_pressed("p"):
        time.sleep(0.1)
    while pausado:
        if keyboard.is_pressed("p"):
            pausado = not pausado
            while keyboard.is_pressed("p"):
                time.sleep(0.1)
        time.sleep(0.1)
    return pausado

def filaCompleta(tablero):
    for y in range(ALTO):
        if all(celda != VACIO for celda in tablero[y]):
            del tablero[y]
            tablero.insert(0, [VACIO for _ in range(ANCHO)])

def finalizarJuego(tablero):
    for y in range(4):
        for x in range(ANCHO):
            if tablero[y][x] != VACIO:
                print("Juego terminado.")
                return True
    return False






def puedeAvanzar(tablero, pieza, x, y):
    # Verifica si la posición siguiente está libre para la pieza
    return y + len(pieza) < ALTO and all(
        tablero[y + 1 + i][x + j] == VACIO 
        for i, fila in enumerate(pieza) 
        for j, celda in enumerate(fila) 
        if celda != VACIO
    )


def validarLogin():
    clear()
    usuario = input("Ingresa tu nombre de usuario: ")
    patron = "(.*[A-Z].*[0-9]|.*[0-9].*[A-Z])"
    while True:
        contrasena = input("Ingresa tu contraseña. Debe contener al menos una mayúscula y un número: ")
        if search(patron, contrasena):
            break
        else:
            print("Contraseña inválida. Debe contener al menos una mayúscula y un número")

def main():
    # validarLogin()
    tablero = crearTablero()
    crearFPS(tablero)



main()