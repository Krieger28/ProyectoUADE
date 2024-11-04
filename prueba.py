import keyboard

# Variable para controlar el estado de la tecla
tecla_presionada = False

def accion(pedro):
    global tecla_presionada
    if not tecla_presionada:
        print("Acción realizada una vez")
        tecla_presionada = True  # Marca que la tecla ha sido presionada

# Función que se ejecuta cuando se suelta la tecla
def liberar_tecla(e):
    global tecla_presionada
    tecla_presionada = False  # Resetea el estado para la próxima vez que se presione

# Asigna una acción a la tecla "a"
keyboard.on_press_key("a", accion)  # Ahora pasamos la función sin paréntesis
keyboard.on_release_key("a", liberar_tecla)  # Lo mismo aquí

# Mantén el programa corriendo
keyboard.wait("esc")
