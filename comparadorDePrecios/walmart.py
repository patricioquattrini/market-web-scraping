from producto import Producto
from bs4 import BeautifulSoup
import requests
from supermercado import Supermercado


class Walmart(Supermercado):

    urlWalmart = "https://www.walmart.com.ar/"
    urlSearchW = "busca/?ft="

    archivo = open('diccWalmart.txt', 'r')
    diccCate = eval(archivo.read())

    def status(self):
        page = requests.get(self.urlWalmart)
        return bool(page.status_code)

    def buscarProductos(self, pedido, cant):

        page = requests.get(self.urlWalmart)
        lista_pWalmart = list()
        pedido = pedido.replace(" ", "+")

        if (page.ok):

            for i in range(1, cant):

                urlF = "{}{}{}&PS=50&O=OrderByNameASC&PageNumber={}".format(self.urlWalmart, self.urlSearchW, pedido, str(i))

                page = requests.get(urlF)
                soup = BeautifulSoup(page.content, "html.parser")

                prices = soup.find_all("span", class_="prateleira__best-price")
                tiltles = soup.find_all("a", class_="prateleira__name")

                tamañoLista = len(prices)

                for j in range(0, tamañoLista):

                    pWalmart = Prducto(nombre=tiltles[j].text, precio=prices[j].text)
                    lista_pWalmart.append(pWalmart)
                if (
                        tamañoLista == 0):  ##Al poner un numero mas grande que la cantidad paginas disponibles, las listas tienen tam 0 pero sigue iterando el i.
                    break
            return lista_pWalmart
        else:
            print("La pagina no funciona")


    def dameProductos(self, cate, cant):

        urlCategoria = self.diccCate.get(cate)
        urlProducto = self.urlWalmart+urlCategoria
        page = requests.get(urlProducto)#############
        lista_pWalmart = list()

        if(page.ok):
            i = 1
            while True:

                arg = "PS=50&O=OrderByNameASC&PageNumber=" + str(i)
                page = requests.get(urlProducto, params=arg)
                if i == 1 and not page.ok:
                    raise Exception("Fallo!!")
                soup = BeautifulSoup(page.content, "html.parser")

                prices = soup.find_all("span", class_="prateleira__best-price")
                tiltles = soup.find_all("a", class_="prateleira__name")

                tamañoLista = len(tiltles)
                print("Pagina "+str(i))

                for j in range(0, tamañoLista):

                    pWalmart = Producto()
                    pWalmart.precio = prices[j].text
                    pWalmart.nombre = tiltles[j].text
                    lista_pWalmart.append(pWalmart)
                if (tamañoLista == 0):##Al poner un numero mas grande que la cantidad paginas disponibles, las listas tienen tam 0 pero sigue iterando el i.
                    break             ##Esto me sirve tambien para salir cuando no existe el producto y no iterar de mas
                i += 1
            return lista_pWalmart