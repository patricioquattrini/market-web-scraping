from producto import Producto
from bs4 import BeautifulSoup
import requests
from supermercado import Supermercado

class Carrefour(Supermercado):

    urlCarrefour = "https://supermercado.carrefour.com.ar/"
    urlSearchC = "catalogsearch/result/?q="

    def status(self):
        return (requests.get(self.urlCarrefour)).ok

    def buscarProductos(self, pedido, lista_pCarrefour):

        #page = requests.get(self.urlCarrefour)

        urlLimpia = self.limpiarURLCarrefour(pedido)

        i = 1
        while True:

            arg = "&order=name&p=" + str(i)
            urlProducto = urlLimpia + arg
            page = requests.get(urlProducto)
            soup = BeautifulSoup(page.content, "html.parser")

            prices = soup.find_all("div", class_="producto-info")
            tiltles = soup.find_all("p", class_="title title-food truncate")
            sinProduc = soup.find_all("img", src="https://supermercado.carrefour.com.ar/skin/frontend/carrefourfood/default/images/search/Error-busqueda.png")

            if(len(sinProduc) != 1):
                tamañoLista = len(prices)

                for j in range(0, tamañoLista):

                    pCarrefour = Producto(nombre=(tiltles[j].text).strip(), precio="$" + prices[j]['data-price'])
                    lista_pCarrefour.append(pCarrefour)

                if (tamañoLista == 0 or (tamañoLista % 10) != 0):  ##Al poner numero mas grande que la cantidad paginas disponibles, el sistema de Carrefour me envia a la ultima pagina donde tiene algun producto
                    break
            else:
                print("NO HAY PRODUCTOS")
                return lista_pCarrefour
            i += 1
        return

    def limpiarURLCarrefour(self, pedido):#Al usar el funcionamiento de Search de Carrefour éste agrega datos de mas en la url impidiendo usarla. Esto lo arregla.
        pedido = pedido.replace(" ", "+")
        urlInput = self.urlCarrefour + self.urlSearchC + pedido

        page = requests.get(urlInput)

        soup = BeautifulSoup(page.content, "html.parser")

        urlProductoSucia = soup.find_all("input", id="login_form_referer")

        urlProducto = urlProductoSucia[0]['value']+"?"
        return urlProducto.replace(":8080", "")