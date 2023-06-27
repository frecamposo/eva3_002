from Producto import *
import random as rn
import numpy as np
ciclo = True
arreglo = np.array([])
##################################################
def salir():
    print("Autor Juanito Simio, 10-10-2050")
    return False


def agregarProducto(arreglo):
    pro = Producto()
    c = False
    while c== False:
        c = pro.setCodigo(input("Ingrese Codigo:"))
    c = False
    while c == False:
        c = pro.setProcedencia(input("Ingrese procedencia:"))
    pro.Tipo = input("ingrese tipo producto:")
    pro.Nombre = input("ingres nombre:")
    c = False
    while c == False:
        try:
            c = pro.setPrecio(int(input("Ingrese precio:")))
        except BaseException as error:
            print(f"Error:{error}")
    pro.Marca = input("ingrese marca:")
    c = False
    while c == False:
        try:
            pro.Stock = int(input("ingrese stock:"))
            c = True
        except BaseException as error:
            print("valor ingresado incorrecto")
    print("producto agregado")
    return np.append(arreglo, pro)


def buscarProducto(arreglo):
    codigo = input("ingrese codigo:")
    for producto in arreglo:
        if producto.Codigo == codigo:
            print(f"Nombre:{producto.Nombre}")
            print(f"Precio:{producto.Precio}")
            print(f"Procedencia:{producto.Procedencia}")


def imprimirMarca(arreglo):
    marca = input("ingrese marca:")
    total = 0
    for producto in arreglo:
        if producto. Marca == marca:
            print(f"Nombre:{producto.Nombre}")
            print(f"Precio:{producto.Precio}")
            total += producto.Precio
    print(f"Total General:{total}")

def imprimirProcedencia(arreglo):
    procedencia = input("ingrese procedencia:")
    total = 0
    for producto in arreglo:
        if producto.Procedencia.upper() == procedencia.upper():
            print(f"Nombre:{producto.Nombre}")
            print(f"Precio:{producto.Precio}")
            total += producto.Precio
    print(f"Total General:{total}")


def imprimirProducto(arreglo):
    print("1) Listado Marca")
    print("2) Listado Procedencia")
    print("3) Listado Codigo Producto")
    try:
        op_list = int(input("Seleccione:"))
        codigo_certi =rn.randint(100,1500)
        match op_list:
            case 1:
                print(f"Certificado por Marca: Codigo.{codigo_certi}")
                imprimirMarca(arreglo)
            case 2:
                print(f"Certificado por Procedencia: Codigo.{codigo_certi}")
                imprimirProcedencia(arreglo)
            case 3:
                print(f"Certificado por Cod.Producto: Codigo.{codigo_certi}")
                buscarProducto(arreglo)
    except BaseException as err:
        print(f"Error:{err}")
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
            case 1:
                print("agregar")
                arreglo = agregarProducto(arreglo)
            case 2:
                print("buscar")
                buscarProducto(arreglo)
            case 3:
                print("imprimir")
                imprimirProducto(arreglo)
            case 4:
                ciclo = salir()
    except BaseException as error:
        print(f"Error:{error}")
