from Producto import *
ciclo = True

##################################################
def salir():
    print("Autor Juanito Simio, 10-10-2050")
    return False

##################################################
while ciclo:
    print("Menu Korea")
    print("1.- Agregar Producto")
    print("2.- Buscar")
    print("3.- Imprimir")
    print("4.- Salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 4:
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")
