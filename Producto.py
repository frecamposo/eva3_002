class Producto:
    Codigo =''
    Tipo=''
    Nombre=''
    Marca=''
    Precio=0
    Stock=0
    Procedencia=''

    def __init__(self):
        self.Codigo='AA001'
        self.Tipo='Electronica'
        self.Nombre='TV'
        self.Marca='S/M'
        self.Precio=500
        self.Stock=1
        self.Procedencia='AMERICA'

    def setProcedencia(self,procedencia):
        if procedencia.upper() == 'AMERICA' or procedencia.upper() == 'ASIA' or procedencia.upper() == 'EUROPA':
            self.Procedencia = procedencia
            return True
        else:
            print("procedencia AMERICA, EUROPA, ASIA")
            return False

    def setCodigo(self,codigo):
        if len(codigo) >= 2 and len(codigo) <= 15:
            self.Codigo = codigo
            return True
        else:
            print("codigo largo entre 2 y 15 caracteres")
            return False
    def setPrecio(self,precio):
        if precio >= 500:
            self.Precio = precio
            return True
        else:
            print("precio mayor o igual a 500")
            return False