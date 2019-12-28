from producto import Producto
from bs4 import BeautifulSoup
import requests
from supermercado import Supermercado


class Walmart(Supermercado):

    urlWalmart = "https://www.walmart.com.ar/"
    urlSearchW = "busca/?ft="

    def status(self):
        page = requests.get(self.urlWalmart)
        return bool(page.status_code)

    def buscarProductos(self, pedido, lista_pWalmart):

        page = requests.get(self.urlWalmart)

        pedido = pedido.replace(" ", "+")

        if (page.ok):
            i = 1
            while True:

                urlF = "{}{}{}&PS=50&O=OrderByNameASC&PageNumber={}".format(self.urlWalmart, self.urlSearchW, pedido, str(i))

                page = requests.get(urlF)
                soup = BeautifulSoup(page.content, "html.parser")

                prices = soup.find_all("span", class_="prateleira__best-price")
                tiltles = soup.find_all("a", class_="prateleira__name")

                tamañoLista = len(prices)

                for j in range(0, tamañoLista):

                    pWalmart = Producto(nombre=tiltles[j].text, precio=prices[j].text)
                    lista_pWalmart.append(pWalmart)
                if (
                        tamañoLista == 0):  ##Al poner un numero mas grande que la cantidad paginas disponibles, las listas tienen tam 0 pero sigue iterando el i.
                    break
                i += 1
            return
        else:
            print("La pagina no funciona")