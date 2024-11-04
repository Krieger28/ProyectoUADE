import keyboard
import time
import os
import random
from re import search


piezas={
    "cuadrado":{
    "estructura":[
        [[1,1],
        [1,1]]
        ],
    "color":"🟨"
    },
    
    "l":{
    "estructura":[
        [[1,0],
         [1,0],
         [1,1]],

        [[1,1,1],
         [1,0,0]],

        [[1,1],
         [0,1],
         [0,1]],

        [[0,0,1],
         [1,1,1]] 
        ],
    "color":"🟧"
    },

    "j":{
    "estructura":[
        [[0,1],
         [0,1],
         [1,1]],

        [[1,0,0],
         [1,1,1]],

        [[1,1],
         [1,0],
         [1,0]],

        [[1,1,1],
         [0,0,1]]
        ],
    "color":"🟫"
    },

    "i":{
    "estructura":[
        [[1,1,1,1]],
        
        [[0,1],
         [0,1],
         [0,1],
         [0,1]],

        [[1,1,1,1]],

        [[1,0],
         [1,0],
         [1,0],
         [1,0]]
        ],
    "color":"🟦"
    },

    "t":{
    "estructura":[
        [[0,1,0],
         [1,1,1]],
        
        [[1,0],
         [1,1],
         [1,0]],

        [[1,1,1],
         [0,1,0]],

        [[0,1],
         [1,1],
         [0,1]]
        ],
    "color":"🟪"
    },

    "z":{
    "estructura":[
        [[1,1,0],
         [0,1,1]],
        
        [[0,1],
         [1,1],
         [1,0]]
        ],
    "color":"🟥"
    },

    "s":{
    "estructura":[
        [[0,1,1],
         [1,1,0]],

        [[1,0],
         [1,1],
         [0,1]]
        ],
    "color":"🟩"
    }
}


clear = lambda: os.system('cls')

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
    pausado = False
    banderaPasadas=True
    while banderaPasadas:  #  vincularlo  con un input del teclado esc o algo asi y el game over
        x, y = 3, 0
        
        PIEZA= piezas[random.choice(list(piezas.keys()))]
        
        if finalizarJuego(tablero):
            banderaPasadas=False
        banderaFPS=True
        while banderaFPS:
            x, y, pausado = inputsTeclado(tablero, PIEZA, x, y, pausado) # Actualiza el estado de pausa y piezas
            if pausado:
                time.sleep(0.1)
                continue

            time.sleep(0.05)            
            clear()
            imprimirTablero(tablero)
            nuevo_x, nuevo_y = moverPiezaAbajo(tablero, PIEZA, x, y)
            if puedeAvanzar(nuevo_y,tablero,nuevo_x)==False:
                filaCompleta(tablero)
                banderaFPS=False 
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
            if x!=VACIO:
                aux+=1
        if aux==10:
            eliminarFila(tablero,y)
            agregarFila(tablero)


def moverPiezaAbajo(tablero, pieza, x, y):
    '''ESTA FUNCION SIMULA LA CAIDA DE UNA PIEZA POR EL TABLERO'''   
    estructura=pieza["estructura"][0]

    for i, fila in enumerate(estructura):
        for j, celda in enumerate(fila):
            if celda == 1:
                if y + i + 1 >= ALTO or tablero[y + i + 1][x + j] != VACIO:
                    return x, y  # Si hay colisión, no se mueve

    # Si ninguna celda choca, entonces se mueve la pieza hacia abajo
    borrarPieza(tablero, pieza, x, y)
    y += 1
    colocarPieza(tablero, pieza, x, y)
    return x, y
    
    
    """
    cantUnos=0
    aux=0
    for i, fila in enumerate(estructura):
        for j, celda in enumerate(fila):
            if celda == 1:
                cantUnos+=1
                if y + i + 1 < ALTO and tablero[y + i + 1][x + j] == VACIO:
                    aux+=1
                    if aux == cantUnos:
                        borrarPieza(tablero, pieza, x, y)
                        y+=1
                        colocarPieza(tablero, pieza, x, y)
                        return x,y
    """

    """
    if y + 1 < ALTO and tablero[y + 1][x] == VACIO:
        borrarPieza(tablero, pieza, x, y)
        y += 1
        colocarPieza(tablero, pieza, x, y)
        return x, y
    return x, y
    """

def borrarPieza(tablero, pieza, x, y):
    '''ESTA FUNCION ELIMINA PIEZAS DE POSICIONES ESPECIFICAS'''
    estructura=pieza["estructura"][0]
    
    for i, fila in enumerate(estructura):  
        for j, celda in enumerate(fila):  
            if celda == 1:  
                tablero[y + i][x + j] = VACIO


def colocarPieza(tablero, pieza, x, y):
    '''ESTA FUNCION COLOCA PIEZAS EN EL TABLERO'''
    estructura=pieza["estructura"][0]
    
    for i, fila in enumerate(estructura):  
        for j, celda in enumerate(fila):  
            if celda == 1:  
                tablero[y + i][x + j] =pieza["color"]



def inputsTeclado(tablero, pieza, x, y, pausado):
    '''ESTA FUNCION PERMITE QUE EL SISTEMA DETECTE LOS IMPUTS DEL USUARIO'''
    if keyboard.is_pressed("space"):
        pass  # bajar más rápido o insta ponerla en donde quedaría
    if keyboard.is_pressed("down"):
        pass  # bajar más rápido o insta ponerla en donde quedaría
    if keyboard.is_pressed("up"):
        pass  # girar pieza
    if keyboard.is_pressed("left"):
        x, y = moverIzq(tablero, pieza, x, y)
    elif keyboard.is_pressed("right"):
        x, y = moverDer(tablero, pieza, x, y)
    
    if keyboard.is_pressed("esc"):
        pass  # cerrar juego, ver de aplicarlo al primer while???
    
    if keyboard.is_pressed("p"):
        pausado = pausa(pausado)  # pausar el juego
    return x, y, pausado


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


def validarLogin():
    '''ESTA FUNCION SE ENCARGA DE GENERAR UN SISTEMA DE LOGIN EL CUAL REQUIERE INTRODUCIR UNA CONTRASEÑA
    CON AL MENOS UNA MAYUSCULA Y UN NUMERO PARA CONTINUAR CON EL PROGRAMA PRINCIPAL'''
    clear()
    usuario = input("Ingresa tu nombre de usuario: ")
    patron = "(.*[A-Z].*[0-9]|.*[0-9].*[A-Z])"
    banderaContrasena=True
    while banderaContrasena:
        contrasena = input("Ingresa tu contraseña. Debe contener al menos una mayuscula y un numero: ")
        
        if search(patron, contrasena):
            banderaContrasena=False
        else:
            print("Contraseña inválida. Debe contener al menos una mayúscula y un número")




    
def finalizarJuego(tablero):
    '''ESTA FUNCION SE ENCARGA DE FINALIZAR EL LOOP PRINCIPAL DEL JUEGO UNA VEZ QUE UNA NUEVA PIEZA NO PUEDA
    INGRESAR EN LAS 20 FILAS INFERIORES DE LA MATRIZ'''
 
    for y in range(4):  
        for x in range(ANCHO):
            if tablero[y][x] != VACIO:  
                print("Juego terminado.")
                return True   
    return False  
 
    # Input para voler a jugar
    


def aumentarVel():
    '''Esta función se encarga de aumentar la velocidad del juego a medida que se eliminen filas'''


def main():
    '''ESTA FUNCION SE ENCARGA DE EJECUTAR EL PROYECTO'''
    #validarLogin()
    tablero = crearTablero()
    crearFPS (tablero)
main()






# Funcion para enviar la pieza al fondo del tablero
# Funcion para crear piezas con sus formas
# Funcion para que seleccione una pieza aleatoria
# Funcion para rotar piezas

