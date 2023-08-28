from Nodo import Nodo
from Graph import Graph
#from colorama import Fore

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
    
    def agregarAlFinal(self, dato): #se implementa en colas (ordenamiento de datos)
        nuevo = Nodo(self.id, dato)
        self.id +=1
        if self.esVacio():
            self.nodoInicial = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size +=1

    def agregarInicio(self, dato): #se implementa en pilas (ordenamiento de matriz)
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.esVacio():
            self.nodoInicial = nuevo
            self.nodoFinal = nuevo
        else:
            nuevo.setSiguiente(self.nodoInicio)
            self.nodoInicio = nuevo
        self.size += 1

    def convertirABinario(self):
        temporal = self.nodoInicial
        while temporal != None:
            if(int(temporal.getDato())>=1):
                temporal.setDato(1)
            temporal = temporal.getSiguiente()
    
    def cargaArchivo():
        pass


    def procesarSalidaBinaria(self): #opcion2
        #temporal = self.nodoInicial
        pass


    #def generarSalidaXML(self): #opcion3
        #actual = self.nodoInicial

        #xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str#('"UTF-8"') + '?>\n'
        #xml += '<senalesReducidas>\n'

        #while actual is not None:
            #xml += '    <senal nombre= "'+actual.getSenalPatron()'"'


    def generarGrafica(self, nombreArchivo, colorNodo): #opcion5
        grafica = Graph(nombreArchivo, colorNodo)
        temporal = self.nodoInicial
        while temporal != None:
            grafica.agregar(temporal, temporal.getSiguiente())
            temporal = temporal.getSiguiente()
        grafica.generar()

    def imprimir(self): #prueba --------------------------------------
        temporal = self.nodoInicial
        while temporal != None:
            print(temporal.getDato())
            temporal = temporal.getSiguiente()