class Producto():

    def __init__(self, nombre=None, precio=None):

        self.nombre = nombre
        self.precio = precio

    def MostrarProducto(self):
        print("Producto {Nombre} {Precio} ".format(Nombre=self.nombre, Precio=self.precio))

    def dameNombreProd(self):
        return self.nombre

    def damePrecioProd(self):
        return self.precio