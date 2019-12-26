from producto import Producto
from bs4 import BeautifulSoup
import requests
from supermercado import Supermercado

class Carrefour(Supermercado):

    urlCarrefour = "https://supermercado.carrefour.com.ar/"
    urlSearchC = "catalogsearch/result/?q="

    def status(self):
        return (requests.get(self.urlCarrefour)).ok

    def buscarProductos(self, pedido):

        page = requests.get(self.urlCarrefour)

        if (page.ok):

            lista_pCarrefour = list()
            urlLimpia = self.limpiarURLCarrefour(pedido)
            i = 1  #Con cada i recorro las paginas con 10 productos
            while True:

                arg = "&order=name&p=" + str(i)
                urlProducto = urlLimpia + arg

                page = requests.get(urlProducto)

                soup = BeautifulSoup(page.content, "html.parser")

                prices = soup.find_all("div", class_="producto-info")
                tiltles = soup.find_all("p", class_="title title-food truncate")
                sinProduc = soup.find_all("img", src="https://supermercado.carrefour.com.ar/skin/frontend/carrefourfood/default/images/search/Error-busqueda.png")

                if(len(sinProduc) != 1):
                    tamañoLista = len(tiltles)

                    print("Pagina " + str(i))

                    for j in range(0, tamañoLista):

                        pCarrefour = Producto(nombre=(tiltles[j].text).strip(), precio="$" + prices[j]['data-price'])
                        lista_pCarrefour.append(pCarrefour)

                    if (tamañoLista == 0 or (tamañoLista % 10) != 0):  ##Al poner numero mas grande que la cantidad paginas disponibles, el sistema de Carrefour me envia a la ultima pagina donde tiene algun producto
                        break
                else:
                    return lista_pCarrefour
                i += 1

        else:
            print("La pagina no funciona")

        return lista_pCarrefour


    def dameProductos(self, cate):

        archivo = open('diccCarrefour.txt', 'r')
        diccCate = eval(archivo.read())
        urlCategoria = diccCate.get(cate)
        urlProducto = self.urlCarrefour+urlCategoria
        page = requests.get(urlProducto)
        lista_pCarrefour = list()

        if(page.ok):

            i = 1 #Con cada i recorro las paginas con 10 productos
            while True:

                arg = "order=name&p=" + str(i)
                page = requests.get(urlProducto, params=arg)
                soup = BeautifulSoup(page.content, "html.parser")

                prices = soup.find_all("div", class_="producto-info")
                tiltles = soup.find_all("p", class_="title title-food truncate")

                tamañoLista = len(tiltles)
                print("Pagina "+str(i))

                for j in range(0, tamañoLista):

                    pCarrefour = Producto(nombre=(tiltles[j].text).strip(), precio="$" + prices[j]['data-price'])
                    lista_pCarrefour.append(pCarrefour)

                if (tamañoLista == 0 or (tamañoLista % 10) != 0): ##Al poner numero mas grande que la cantidad paginas disponibles, el sistema de Carrefour me envia a la ultima pagina donde tiene algun producto
                    break
                i += 1
        else:
            print("La pagina no funciona")
        return lista_pCarrefour

    def limpiarURLCarrefour(self, pedido):#Al usar el funcionamiento de Search de Carrefour éste agrega datos de mas en la url impidiendo usarla. Esto lo arregla.
        pedido = pedido.replace(" ", "+")
        urlInput = self.urlCarrefour + self.urlSearchC + pedido

        page = requests.get(urlInput)

        soup = BeautifulSoup(page.content, "html.parser")

        urlProductoSucia = soup.find_all("input", id="login_form_referer")

        urlProducto = urlProductoSucia[0]['value']
        return urlProducto.replace(":8080", "")