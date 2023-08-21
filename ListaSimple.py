from Nodo import Nodo
from Graph import Graph


class ListaSimple():
    id=0
    def __init__(self):
        self.nodoInicial = None
        self.nodoFinal = None
        self.size = 0

    def getInicial(self):
        return self.nodoInicial
    
    def esVacio(self):
        return self.size == 0
    
    def agregarFinal(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id +=1
        if self.esVacio():
            self.nodoInicial = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size +=1
    
    def cargaArchivo():
        pass


    def procesarArchivo(self):
        #temporal = self.nodoInicial
        pass


    def generarSalidaXML(self): #opcion3
        actual = self.nodoInicial

        xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n'
        xml += '<senalesReducidas>\n'

        #while actual is not None:
            #xml += '    <senal nombre= "'+actual.getSenalPatron()'"'
    
    def generarGrafica(self): #opcion5
        grafica = Graph()
        temporal = self.nodoInicial
        while temporal != None:
            grafica.add(temporal, temporal.getSiguiente())
            temporal = temporal.getSiguiente()