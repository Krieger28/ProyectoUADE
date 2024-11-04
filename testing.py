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

          [[I, I, I, I]]],

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

def crearTablero():
    return [[VACIO for _ in range(ANCHO)] for _ in range(ALTO)]

def imprimirTablero(tablero):
    print("+" + "--" * ANCHO + "+")
    for i, fila in enumerate(tablero):
        if i >= 0:  # Evita imprimir las primeras 4 filas
            print("|" + "".join(fila) + "|")
    print("+" + "--" * ANCHO + "+")

def seleccionarPieza():
    
    tipo_pieza = random.choice(list(PIEZAS.keys()))
    rotaciones = PIEZAS[tipo_pieza]
    print(tipo_pieza)
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

    #rotacion_inicial = random.choice(rotaciones)
    rotacion_inicial = rotaciones[0]
   

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

def rotarPieza(pieza_actual, tipo_pieza):
    rotaciones = PIEZAS[tipo_pieza]
    indice_actual = rotaciones.index(pieza_actual)
    return rotaciones[(indice_actual + 1) % len(rotaciones)]

def inputsTeclado(tablero, pieza, x, y, pausado, tipo_pieza, color):
    if keyboard.is_pressed("up"):
        borrarPieza(tablero, pieza, x, y)
        pieza = rotarPieza(pieza, tipo_pieza)
        colocarPieza(tablero, pieza, x, y, color)
    # if keyboard.is_pressed("left"):
    #     x, y = moverIzq(tablero, pieza, x, y, color)
    # elif keyboard.is_pressed("right"):
    #     x, y = moverDer(tablero, pieza, x, y, color)
    if keyboard.is_pressed("p"):
        pausado = pausa(pausado)
    return x, y, pausado, pieza, color

# def moverIzq(tablero, pieza, x, y, color):
#     if x - 1 >= 0 and all(tablero[y + i][x - 1 + j] == VACIO for i, fila in enumerate(pieza) for j, celda in enumerate(fila) if celda == PIEZA):
#         borrarPieza(tablero, pieza, x, y)
#         x -= 1
#         colocarPieza(tablero, pieza, x, y, color)
#     return x, y 

# def moverDer(tablero, pieza, x, y, color):
#     if x + len(pieza[0]) < ANCHO and all(tablero[y + i][x + 1 + j] == VACIO for i, fila in enumerate(pieza) for j, celda in enumerate(fila) if celda == PIEZA):
#         borrarPieza(tablero, pieza, x, y)
#         x += 1
#         colocarPieza(tablero, pieza, x, y, color)
#     return x, y 

def moverPiezaAbajo(tablero, pieza, x, y, color):
    # Verifica si hay espacio para mover la pieza hacia abajo
    if y + len(pieza) < ALTO and all(
        tablero[y + 1 + i][x + j] == VACIO 
        for i, fila in enumerate(pieza) 
        for j, celda in enumerate(fila) 
        if celda != VACIO
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



def crearFPS(tablero):
    pausado = False
    while True:
        pieza, tipo_pieza, color = seleccionarPieza()
        x, y = ANCHO // 2, 0

        if finalizarJuego(tablero):
            break

        while True:
            x, y, pausado, pieza, color = inputsTeclado(tablero, pieza, x, y, pausado, tipo_pieza, color)
            if pausado:
                time.sleep(0.1)
                continue

            # Control de movimiento hacia abajo
            time.sleep(0.1)  # Ajusta la velocidad de caída de la pieza
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