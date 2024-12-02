import json
import os

def test_usuariosVacios():
    try:
        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r") as archivo:
                 usuarios = json.load(archivo)
            for usuario in usuarios:  # Accedemos a los valores del diccionario
                assert usuario != ""

                             
    except AssertionError:
       
        assert False
    


    # def test_usuariosVacios():
    # try:
    #     if os.path.exists("usuarios.json"):
    #         with open("usuarios.json", "r") as archivo:
    #             usuario = ""
    #             archivoo = json.load(archivo)
    #             for i in archivoo :
    #                 assert usuario != archivoo[i]




    # except AssertionError:
       
    #     return False