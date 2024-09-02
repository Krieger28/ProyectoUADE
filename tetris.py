# Funcion para generar un tablero

ancho = 10
alto = 20

def imprimirTablero(tablero):
    print("+" + "-" * alto + "+") # Borde de arriba

    for fila in tablero:
        print("|" + "".join(fila) + "|")  # Filas del tablero

    print("+" + "-" * alto + "+") # Borde de abajo

def crearTablero():
    return [[" " for _ in range(alto)] for _ in range(ancho)]

# Funcion para crear piezas con sus formas

# Funcion para que seleccione una pieza aleatoria

# Funcion para que se coloque la pieza en el tablero

# Funcion para que se detecte los inputs del usuario

# Funcion para rotar piezas 

# Funcion para detectar si una celda del tablero esta ocupada

# Funcion para simular la caida de la pieza manual y automaticamente

# Funcion para que detecte en el tablero si una fila esta completa

# Funcion para que si una pieza no puede ingresar al tablero por estar lleno de por finalizado el juego

def main():
    tablero = crearTablero()
    imprimirTablero(tablero)

main()
