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

    "I": [[[I, I, I, I]],
          
          [[I],
           [I],
           [I],
           [I]],


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
           
    "L": [[[VACIO, VACIO, L],
           [L, L, L]],
           
           [[L, VACIO],
           [L, VACIO],
           [L, L]],

          [[L, L, L],
           [L, VACIO, VACIO]],

          [[L, L],
           [VACIO, L],
           [VACIO, L]]

          ],
           
    "J": [
          [[J, VACIO, VACIO],
           [J, J, J]],

          [[J, J],
           [J, VACIO],
           [J, VACIO]],

          [[J, J, J],
           [VACIO, VACIO, J]],

           [[VACIO, J],
           [VACIO, J],
           [J, J]]],

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

puntaje = 0
lineas_Totales = 0

def validarLogin():
    '''ESTA FUNCION SE ENCARGA DE GENERAR UN SISTEMA DE LOGIN EL CUAL REQUIERE INTRODUCIR UNA CONTRASEÑA
    CON AL MENOS UNA MAYUSCULA Y UN NUMERO PARA CONTINUAR CON EL PROGRAMA PRINCIPAL'''
    clear()
    usuario = input("Ingresa tu nombre de usuario: ")
    patron = "(.*[A-Z].*[0-9]|.*[0-9].*[A-Z])"
    banderaContrasena= True
    while banderaContrasena:
        contrasena = input("Ingresa tu contraseña. Debe contener al menos una mayúscula y un número: ")
        if search(patron, contrasena):
            banderaContrasena=False
        else:
            print("Contraseña inválida. Debe contener al menos una mayúscula y un número")

def crearTablero():
    '''ESTA FUNCION GENERA UN TABLERO DE 10 COLUMNAS POR 24 FILAS'''
    return [[VACIO for _ in range(ANCHO)] for _ in range(ALTO)]

def imprimirTablero(tablero):
    '''ESTA FUNCION IMPRIME EL TABLERO GENERADO SIN IMPRIMIR LAS PRIMERAS 4 FILAS'''
    print("+" + "--" * ANCHO + "+")
    for i, fila in enumerate(tablero):
        if i >= 0:  # Evita imprimir las primeras 4 filas
            print("|" + "".join(fila) + "|")
    print("+" + "--" * ANCHO + "+")
    print(f"Puntaje: {puntaje}")  


def crearFPS(tablero):
    '''ESTA FUNCION SE ENCARGA DE RENDEREAR LOS CAMBIOS A LA MATRIZ. SE TRATA DE UN BUCLE INFINITO CONTROLADO QUE CORRE EL PROGRAMA'''
    pausado = False
    banderaPasadas=True
    while banderaPasadas:
        pieza, tipo_pieza, color = seleccionarPieza()
        
        x, y = 3, 0

        if finalizarJuego(tablero):
            banderaPasadas=False
            #clear()
            print("Juego terminado.")
            continue

        banderaFPS = True
        while banderaFPS:
            x, y, pausado, pieza, color = inputsTeclado(tablero, pieza, x, y, pausado, tipo_pieza, color)
            if pausado:
                time.sleep(0.1)
                continue

            # Control de movimiento hacia abajo
            time.sleep(0.3)  # Ajusta la velocidad de caída de la pieza
            clear()
            
            imprimirTablero(tablero)
            borrarPieza(tablero, pieza, x, y)

            # Verificar si puede avanzar, y mover hacia abajo
            if puedeAvanzar(tablero, pieza, x, y):
                x, y = moverPiezaAbajo(tablero, pieza, x, y, color)
            else:
                colocarPieza(tablero, pieza, x, y, color)
                actualizarPuntaje(filaCompleta(tablero))
                banderaFPS=False

            #colocarPieza(tablero, pieza, x, y, color)
def actualizarPuntaje(filas_eliminadas):
    global puntaje
    if filas_eliminadas > 0:
        puntaje += 100 * (2 ** (filas_eliminadas - 1))

def seleccionarPieza():
    '''ESTA FUNCION SE ENCARGA DE SELECCIONAR UNA PIEZA ALEATORIA Y CICLARLAS DE UNA FORMA DETERMINADA'''
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

def puedeAvanzar(tablero, pieza, x, y):
    '''ESTA FUNCION VERIFICA SI HAY ESPACIO PARA MOVER LA PIEZA HACIA ABAJO'''
    return y + len(pieza) < ALTO and all(
        tablero[y + 1 + i][x + j] == VACIO 
        for i, fila in enumerate(pieza) 
        for j, celda in enumerate(fila) 
        if celda != VACIO
    )
    # Distinta forma de hacer lo mismo
    """
    if y + len(pieza) >= ALTO:
        return False
    
    for i, fila in enumerate(pieza): 
        for j, celda in enumerate(fila):
            if celda != VACIO:
                if tablero[y + 1 + i][x + j] != VACIO:
                    return False
    return True
    """

def moverPiezaAbajo(tablero, pieza, x, y, color):
    '''ESTA FUNCION MUEVE LA PIEZA UNA POSICION HACIA ABAJO'''
    borrarPieza(tablero, pieza, x, y)
    y += 1
    colocarPieza(tablero, pieza, x, y, color)
    return x, y

def borrarPieza(tablero, pieza, x, y):
    '''ESTA FUNCION ELIMINA PIEZAS DEL TABLERO'''
    for i, fila in enumerate(pieza):
        for j, celda in enumerate(fila):
            if celda != VACIO and 0 <= x + j < ANCHO and 0 <= y + i < ALTO:
                tablero[y + i][x + j] = VACIO

def colocarPieza(tablero, pieza, x, y, color):
    '''ESTA FUNCION COLOCA PIEZAS EN EL TABLERO'''
    for i, fila in enumerate(pieza):
        for j, celda in enumerate(fila):
            if celda != VACIO and 0 <= x + j < ANCHO and 0 <= y + i < ALTO:
                tablero[y + i][x + j] = color

def filaCompleta(tablero):
    '''ESTA FUNCION DETECTA SI UNA FILA ESTA COMPLETA, EN CASO DE HABER FILAS COMPLETAS, 
    LAS ELIMINA Y AGREGA FILAS NUEVAS EN LA PARTE ALTA DEL TABLERO'''
    global lineas_Totales
    filas_eliminadas = 0
    for y in range(ALTO):
        if all(celda != VACIO for celda in tablero[y]):
            del tablero[y]
            tablero.insert(0, [VACIO for _ in range(ANCHO)])
            filas_eliminadas += 1
            lineas_Totales += 1
    return filas_eliminadas







bandera_rotar = True
bandera_caida = True
def inputsTeclado(tablero, pieza, x, y, pausado, tipo_pieza, color):
    '''ESTA FUNCION PERMITE QUE EL SISTEMA DETECTE LOS IMPUTS DEL USUARIO'''
    global bandera_rotar, bandera_caida
    if keyboard.is_pressed("up"):
        if bandera_rotar:
            borrarPieza(tablero, pieza, x, y)
            pieza, x, y = rotarPieza(tablero, pieza, tipo_pieza, x, y)
            colocarPieza(tablero, pieza, x, y, color)
            bandera_rotar = False
    else:
        bandera_rotar = True
    if keyboard.is_pressed("left"):
        borrarPieza(tablero, pieza, x, y)
        x, y = moverIzq(tablero, pieza, x, y)
        colocarPieza(tablero, pieza, x, y, color)
    if keyboard.is_pressed("right"):
        borrarPieza(tablero, pieza, x, y)
        x, y = moverDer(tablero, pieza, x, y)
        colocarPieza(tablero, pieza, x, y, color)
    if keyboard.is_pressed("space"):
        if bandera_caida:
            borrarPieza(tablero, pieza, x, y)
            x, y = forzarCaida(tablero, pieza, x, y)
            colocarPieza(tablero, pieza, x, y, color)
            bandera_caida = False
    else:
        bandera_caida = True
    if keyboard.is_pressed("p"):
        pausado = pausa(pausado)
    return x, y, pausado, pieza, color


def rotarPieza(tablero, pieza_actual, tipo_pieza, x, y):
    '''ESTA FUNCION SE ENCARGA DE COMPROBAR SI UNA PIEZA PUEDE ROTAR, EN CASO DE SER POSIBLE, LA ROTA'''
    rotaciones = PIEZAS[tipo_pieza]
    indice_actual = rotaciones.index(pieza_actual)
    pieza_rotada = rotaciones[(indice_actual + 1) % len(rotaciones)]
    
    # Evita que la pieza se vaya de los margenes del tablero al rotarla
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

def moverIzq(tablero, pieza, x, y):
    # Verifica si puede mover la pieza hacia la izquierda y la mueve
    if all(
        x > 0 and (tablero[y + i][x - 1 + j] == VACIO or pieza[i][j] == VACIO) 
        for i, fila in enumerate(pieza) 
        for j, celda in enumerate(fila) 
        if celda != VACIO    
    ):
        x -= 1
    return x, y

def moverDer(tablero, pieza, x, y):
    # Verifica si puede mover la pieza hacia la derecha y la nueve
    if all(
        x + len(pieza[0]) < ANCHO and (tablero[y + i][x + j + 1] == VACIO or pieza[i][j] == VACIO) 
        for i, fila in enumerate(pieza) 
        for j, celda in enumerate(fila) 
        if celda != VACIO
    ):
        x += 1
    return x, y

def forzarCaida(tablero, pieza, x, y):
    '''FUEZA LA CAIDA DE LA PIEZA HACIA EL FONDO DEL TABLERO'''
    while y + len(pieza) < ALTO and all(
        tablero[y + 1 + i][x + j] == VACIO 
        for i, fila in enumerate(pieza) 
        for j, celda in enumerate(fila) 
        if celda != VACIO
    ):
        y += 1
    return x, y

def pausa(pausado): 
    '''ESTA FUNCION PAUSA EL JUEGO'''
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

def finalizarJuego(tablero):
    '''ESTA FUNCION SE ENCARGA DE FINALIZAR EL LOOP PRINCIPAL DEL JUEGO UNA VEZ QUE UNA NUEVA PIEZA NO PUEDA
    INGRESAR EN LAS 20 FILAS INFERIORES DE LA MATRIZ'''
    for y in range(4):
        for x in range(ANCHO):
            if tablero[y][x] != VACIO:
                return True
    return False





def main():
    '''ESTA FUNCION SE ENCARGA DE EJECUTAR EL PROYECTO'''
    # validarLogin()
    tablero = crearTablero()
    crearFPS(tablero)


main()