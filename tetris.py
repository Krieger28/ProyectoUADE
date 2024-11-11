
import keyboard
import time
import os
import random
from re import search
import json

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

DISPLAY_ANCHO = 6
DISPLAY_ALTO = 4


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
random.shuffle(listaPiezas)


prox_Pieza = []
puntaje = 0
lineas_Totales = 0
nivel = 1
FPS_inicial = 0.3

def cargarUsuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    else:
        return {}

# Funcion para guardar los usuarios en un archivo JSON
def guardarUsuarios(usuarios):
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

# Funcion para registrar un nuevo usuario
def registrarUsuario():
    clear()
    print("Registrarse")
    usuario = input("Ingresa tu nombre de usuario: ")
    while usuario in cargarUsuarios():
        print("El nombre de usuario ya existe. Intenta otro.")
        usuario = input("Ingresa tu nombre de usuario: ")
    patron = "(.*[A-Z].*[0-9]|.*[0-9].*[A-Z])"
    banderaContrasena= True
    while banderaContrasena:
        contrasena = input("Ingresa tu contraseña (Debe contener al menos una mayuscula y un numero): ")
        if search(patron, contrasena):
            banderaContrasena= False
        else:
            print("Contraseña invalida. Debe contener al menos una mayuscula y un numero.")
    usuarios = cargarUsuarios()
    usuarios[usuario] = {"contrasena": contrasena, "puntajes": []}
    guardarUsuarios(usuarios)
    return usuario

# Funcion para iniciar sesion con un usuario existente
def iniciarSesion():
    clear()
    print("Iniciar sesion")
    
    banderaUsuario = True
    while banderaUsuario:
        usuario = input("Ingresa tu nombre de usuario: ")
        usuarios = cargarUsuarios()
        if usuario in usuarios:
            banderaUsuario = False
        else:
            print("El usuario no existe. Intenta nuevamente.")
    
    banderaContrasena = True
    while banderaContrasena:
        contrasena = input("Ingresa tu contraseña: ")
        if contrasena == usuarios[usuario]["contrasena"]:
            banderaContrasena = False
        else:
            print("Contraseña incorrecta. Ingresela nuevamente.")
    
    return usuario


# Funcion para guardar el puntaje del usuario
def guardarPuntaje(usuario, puntaje):
    usuarios = cargarUsuarios()
    usuarios[usuario]["puntajes"].append(puntaje)
    guardarUsuarios(usuarios)


# Funcion para mostrar los tres mejores puntajes de un usuario
def mostrarMejoresPuntajes(usuario):
    usuarios = cargarUsuarios()
    puntajes = sorted(usuarios[usuario]["puntajes"], reverse=True)
    print(f"{usuario} - Mejores puntajes:")
    for i, puntaje in enumerate(puntajes[:3]):
        print(f"{i + 1}) {puntaje}")

def crearTablero():
    '''ESTA FUNCION GENERA UN TABLERO DE 10 COLUMNAS POR 24 FILAS'''
    return [[VACIO for _ in range(ANCHO)] for _ in range(ALTO)]

def CrearProxPiezaDisplay():
    '''ESTA FUNCION GENERA UN TABLERO DE 6 COLUMNAS POR 6 FILAS'''
    global DISPLAY_ANCHO
    global DISPLAY_ALTO
    return [[VACIO for _ in range(DISPLAY_ANCHO)] for _ in range(DISPLAY_ALTO)]




def imprimirTablero(tablero, piezaDisplay):
    '''Imprime el tablero principal de 20 filas y a la derecha un tablero pequeño de 4 filas.'''


    
    print("+" + "--" * ANCHO + "+" + "   " + "+" + "--" * DISPLAY_ANCHO + "+")
    
    for i in range(20): 
    
        fila_principal = "|" + "".join(tablero[i + 4]) + "|"
        
        if i < DISPLAY_ALTO:
            fila_pieza_display = "|" + "".join(piezaDisplay[i]) + "|"
        else:
            if i == DISPLAY_ALTO:
                fila_pieza_display =  "+" + "--" * DISPLAY_ANCHO + "+"
            else:
                if i == DISPLAY_ALTO + 4:
                    fila_pieza_display =  f"NIVEL: {nivel}"
                else:
                    if i == DISPLAY_ALTO + 6:
                        fila_pieza_display =  f"PUNTOS: {puntaje}"
                    else:
                        fila_pieza_display = " " * (DISPLAY_ANCHO * 2 + 2)


        print(fila_principal + "   " + fila_pieza_display)


    print("+" + "--" * ANCHO + "+")
    
 

















def crearFPS(tablero, piezaDisplay):
    '''ESTA FUNCION SE ENCARGA DE RENDEREAR LOS CAMBIOS A LA MATRIZ. SE TRATA DE UN BUCLE INFINITO CONTROLADO QUE CORRE EL PROGRAMA'''
    pausado = False
    banderaPasadas=True

    global prox_Pieza
    global nivel
    global lineas_Totales
    global FPS_inicial
    while banderaPasadas:
        x, y = 3, 0
        pieza, tipo_pieza, color = seleccionarPieza()
        
        seleccionarProxPiezaYcolocar(piezaDisplay, color)
        if finalizarJuego(tablero):
            banderaPasadas=False
            #clear()
            print("Juego terminado.")
            break
        

        Niveles()
        banderaFPS = True
        while banderaFPS:
            x, y, pausado, pieza, color = inputsTeclado(tablero, pieza, x, y, pausado, tipo_pieza, color)
            if pausado:
                time.sleep(0.1) 
                continue

            # Control de movimiento hacia abajo
            
           
            time.sleep(FPS_inicial)  # Ajusta la velocidad de caída de la pieza
            clear()
            
            imprimirTablero(tablero, piezaDisplay)
            borrarPieza(tablero, pieza, x, y)

            # Verificar si puede avanzar, y mover hacia abajo
            if test_moverPiezaAbajo(tablero, pieza, x, y, color):
                x, y = moverPiezaAbajo(tablero, pieza, x, y, color)
            else:
                colocarPieza(tablero, pieza, x, y, color)
                actualizarPuntaje(filaCompleta(tablero))
                banderaFPS=False












def actualizarPuntaje(filas_eliminadas):
    global puntaje
    if filas_eliminadas > 0:
        puntaje += 100 * (2 ** (filas_eliminadas - 1))



def Niveles():
    """ESTA FUNCION RECIBE LA VELOCIDAD Y CUANDO EL NIVEL SUBE, EDITA PARA AUMENTAR LA DIFICULTAD"""
    global nivel
    global lineas_Totales
    global FPS_inicial

    if lineas_Totales >= 2:
        lineas_Totales = 0
        nivel += 1
        FPS_inicial = FPS_inicial * 0.5
    return FPS_inicial



def Randomizar_Lista(prevPiezas):
    global listaPiezas
    randomlistas = list(PIEZAS.keys())
    
    random.shuffle(randomlistas) 
    
    listaPiezas = randomlistas + prevPiezas 



def seleccionarPieza():
    '''ESTA FUNCION SE ENCARGA DE SELECCIONAR UNA PIEZA ALEATORIA Y CICLARLAS DE UNA FORMA DETERMINADA'''
    global listaPiezas


    tipo_pieza = listaPiezas[ len(listaPiezas)-1] 
    rotaciones = PIEZAS[tipo_pieza]
    rotacion_inicial = rotaciones[0]

    listaPiezas.pop(len(listaPiezas)-1)
    
    if len(listaPiezas)==1:
        Randomizar_Lista(listaPiezas)
    
    
    
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




def seleccionarProxPiezaYcolocar(piezaDisplay, color):
    '''ESTA FUNCION SE ENCARGA DE SELECCIONAR UNA PIEZA ALEATORIA Y CICLARLAS DE UNA FORMA DETERMINADA'''
    global listaPiezas
    global prox_Pieza


    for i in range(DISPLAY_ALTO):
        for j in range(DISPLAY_ANCHO):
            piezaDisplay[i][j] = VACIO


    tipo_pieza = listaPiezas[-1] 
    rotaciones = PIEZAS[tipo_pieza]
    prox_Pieza = rotaciones[0] 





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



    for i, fila in enumerate(prox_Pieza):
        for j, celda in enumerate(fila):
            if celda != VACIO:
                piezaDisplay[i +1][j + (DISPLAY_ANCHO - len(fila)) // 2] = color

    


    







def moverPiezaAbajo(tablero, pieza, x, y, color):
    '''ESTA FUNCION MUEVE LA PIEZA UNA POSICION HACIA ABAJO'''
    borrarPieza(tablero, pieza, x, y)
    y += 1
    colocarPieza(tablero, pieza, x, y, color)
    return x, y

def test_moverPiezaAbajo(tablero, pieza, x, y, color):
    '''ESTA FUNCION VERIFICA SI HAY ESPACIO PARA MOVER LA PIEZA HACIA ABAJO'''
    try:
       
        assert y + len(pieza) < ALTO and all(
            tablero[y + 1 + i][x + j] == VACIO 
            for i, fila in enumerate(pieza) 
            for j, celda in enumerate(fila) 
            if celda != VACIO
        )

        assert color != VACIO
       
        return True
    except AssertionError:
       
        return False


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
    global nivel
    global bandera_rotar, bandera_caida
    if keyboard.is_pressed("up"):
        if nivel == 1:
            borrarPieza(tablero, pieza, x, y)
            pieza, x, y = rotarPieza(tablero, pieza, tipo_pieza, x, y)
            colocarPieza(tablero, pieza, x, y, color)
        else:
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
    print("Bienvenido a Tetris!")
    banderaBienvenida=True
    while banderaBienvenida:
        opcion = input("¿Tienes cuenta? (s/n): ")
        if opcion.lower() == "n":
            usuario = registrarUsuario()
            banderaBienvenida=False
        if opcion.lower() == "s":
            usuario = iniciarSesion()
            banderaBienvenida=False
        else:
            print("Opcion invalida. Introduzca una opocion vailda")        
    piezaDisplay = CrearProxPiezaDisplay()
    tablero = crearTablero()
    crearFPS(tablero, piezaDisplay)
    guardarPuntaje(usuario, puntaje)
    mostrarMejoresPuntajes(usuario)

main()