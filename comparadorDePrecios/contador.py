from carrefour import Carrefour
from walmart import Walmart
from prettytable import PrettyTable

def MostrarProductos(productos):
    count = 0
    for producto in productos:
        count += 1
        producto.MostrarProducto()
    print("Total productos: "+str(count))

##Cerveza // Fernet // Agua // Vino // Sidras y Espumantes

carrefour = Carrefour()
#produc = input("Ingresar Producto ")
#listaCarrefour1 = carrefour.dameProductos("Agua", 1000)
#listaCarrefour = carrefour.buscarProductos(produc, 100)
#MostrarProductos(listaCarrefour)

walmart = Walmart()
listaWalmart = walmart.dameProductos("Cerveza", 1000)
#listaWalmart = walmart.buscarProductos("pepsi", 10)
MostrarProductos(listaWalmart)


"""
listaCarrefour = listaWalmart

tamListWalrmart = len(listaWalmart)
listaCarrefour = listaWalmart
listaCarrefour.pop()
listaCarrefour.pop()
tamListCarrefour = len(listaCarrefour)


outTbl = PrettyTable(["Producto Carrefour", "Precio", "Precio", "Producto Walmart"])

for i in range(0, max(tamListCarrefour, tamListWalrmart)):
    if i > tamListCarrefour-1:
        outTbl.add_row([" ",
                        " ",
                        listaWalmart[i].precioProducto(),
                        listaWalmart[i].nombreProducto()])
    elif i > tamListWalrmart-1:
        outTbl.add_row([listaCarrefour[i].nombreProducto(),
                        listaCarrefour[i].precioProducto(),
                        " ",
                        " "])
    else:
        outTbl.add_row([listaCarrefour[i].nombreProducto(),
                        listaCarrefour[i].precioProducto(),
                        listaWalmart[i].precioProducto(),
                        listaWalmart[i].nombreProducto()])

print(outTbl)
"""