from prettytable import PrettyTable

def mostrarListasDeProductos(listaWalmart, listaCarrefour):

    tamListWalrmart = len(listaWalmart)
    tamListCarrefour = len(listaCarrefour)
    outTbl = PrettyTable(["Carrefour", "Precios Carrefour", "Precios Walmart", "Walmart"])

    print("Cant Carrefour "+str(tamListCarrefour)+" Cant Walmart "+str(tamListWalrmart))

    if(tamListCarrefour > tamListWalrmart):

        for i in range(0, tamListCarrefour):
            if (i < tamListWalrmart - 1):
                outTbl.add_row([listaCarrefour[i].dameNombreProd(),
                                listaCarrefour[i].damePrecioProd(),
                                listaWalmart[i].damePrecioProd(),
                                listaWalmart[i].dameNombreProd()])
            if(i > tamListWalrmart-1):
                outTbl.add_row([listaCarrefour[i].dameNombreProd(),
                                listaCarrefour[i].damePrecioProd(),
                                "-",
                                "-"])

        if (tamListCarrefour < tamListWalrmart):

            for i in range(0, tamListWalrmart):
                if (i < tamListCarrefour-1):
                    outTbl.add_row([listaCarrefour[i].dameNombreProd(),
                                    listaCarrefour[i].damePrecioProd(),
                                    listaWalmart[i].damePrecioProd(),
                                    listaWalmart[i].dameNombreProd()])
                if (i > tamListCarrefour-1):
                    outTbl.add_row(["-",
                                    "-",
                                    listaWalmart[i].precioProducto(),
                                    listaWalmart[i].nombreProducto()])

        if (tamListCarrefour == tamListWalrmart):
            for i in range(0, tamListCarrefour):
                outTbl.add_row([listaCarrefour[i].dameNombreProd(),
                            listaCarrefour[i].damePrecioProd(),
                            listaWalmart[i].damePrecioProd(),
                            listaWalmart[i].dameNombreProd()])
    print(outTbl)

def mostrarListaDeProductos(listaDeProductos):

    for producto in listaDeProductos:
        print(producto.dameNombreProd()+"--"+producto.damePrecioProd())