from carrefour import Carrefour
from walmart import Walmart
from mostrarProductos import mostrarListasDeProductos
from mostrarProductos import mostrarListaDeProductos
import threading

while True:

    carrefour = Carrefour()
    walmart = Walmart()
    print("INGRESE UN PRODUCTO ")
    producto = input()
    listaCarrefour = list()
    listaWalmart = list()

    hilo_1 = threading.Thread(name="hilo_1", target=carrefour.buscarProductos, args=(producto, listaCarrefour))
    hilo_2 = threading.Thread(name="hilo_2", target=walmart.buscarProductos, args=(producto, listaWalmart))

    hilo_1.start()
    hilo_2.start()

    hilo_1.join()
    hilo_2.join()

    mostrarListasDeProductos(listaWalmart, listaCarrefour)
    # print("CARREFOUR")
    #mostrarListaDeProductos(listaCarrefour)
    #print("   ")
    # print("WALMART")
    # mostrarListaDeProductos(listaWalmart)
    print("PRESIONE 0 PARA SALIR O 1 PARA VOLVER")
    op = input()
    if (int(op) == 0):
        break
