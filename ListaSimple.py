from Nodo import *
from Graph import Graph
#from Senal import Senal
from colorama import Fore, init
init()
from Senal import *
#from LecturaXML import LecturaXML
#from Tiempo import Tiempo
#from SenalesReducidas import SenalesReducidas

class ListaSimple():
    id=0
    def __init__(self):
        self.nodoInicial = None
        self.nodoFinal = None
        self.size = 0
        #self.otro = SenalesReducidas()
        #self.senales = LecturaXML()

    def getInicial(self):
        return self.nodoInicial
    
    def esVacio(self):
        return self.nodoInicial == None
    
    def agregarAlFinal(self, dato): # agregar / senal
        nuevo = Nodo(self.id, dato)
        self.id +=1
        if self.esVacio():
            self.nodoInicial = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size +=1

    def buscarSenal(self, nombre):
        actual = self.nodoInicial
        while actual:
            if actual.dato.nombre == nombre:
                return actual.dato
            actual = actual.siguiente
        return None

    def convertirABinario(self):
        temporal = self.nodoInicial
        while temporal != None:
            if(int(temporal.getDato())>=1):
                temporal.setDato(1)
            temporal = temporal.getSiguiente()
    
    def listaSenalesXML(self): # lista de senales ## desde un return
        print("_____Lista de senales_____")
        senalGuardada = self.nodoInicial
        while senalGuardada is not None:
            nombre = senalGuardada.getDato().getNombre()
            tiempoMaximo = senalGuardada.getDato().getTiempoMaximo()
            amplitudMaxima = senalGuardada.getDato().getAmplitudMaxima()
            print(nombre)
            print(tiempoMaximo)
            print(amplitudMaxima)
            senalGuardada = senalGuardada.getSiguiente()

    def listaTiemposXML(self): # lista de tiempos
        print("_____Lista de tiempos_____")
        objetoTiempo = self.nodoInicial
        while objetoTiempo != None:
            tiempo =  objetoTiempo.getDato().getTiempo()
            #tiempo =  senalGuardada.getDato().getTiempo()
            amplitud =  objetoTiempo.getDato().getAmplitud()
            print(tiempo)
            print(amplitud)
            objetoTiempo = objetoTiempo.getSiguiente()

    def listaAmplitudesXML(self): # lista de amplitudes
        print("_____Lista de amplitudes_____")
        objetoAmplitud = self.nodoInicial
        while objetoAmplitud != None:
            #amplitud = objetoAmplitud.getDato().getAmplitud()
            dato =  objetoAmplitud.getDato().getDato()
            #print(amplitud)
            print(dato)
            objetoAmplitud = objetoAmplitud.getSiguiente()
    
    def soloTiemposx(self): # lista de amplitudes
        print("_____Lista de tiempossssss_____")
        tmp = self.nodoInicial
        while tmp != None:
            #amplitud = tmp.getDato().getAmplitud()
            tiempo =  tmp.getDato().getTiempo()
            dato =  tmp.getDato().getAmplitud()
            #print(amplitud)
            print(tiempo)
            print(dato)
            tmp = tmp.getSiguiente()

    def soloTiempos(self): # lista de amplitudes
        print("_____Lista de solo tiempossssss_____")
        tmp = self.nodoInicial
        while tmp != None:
            tmp.getDato().getAmplitud()
            tmp = tmp.getSiguiente()
        return tmp
        
    def agruparSenalesBinarias(self):
        listaSenales = self.listaSenalesXML()
        listaTiempos = self.listaTiemposXML()
        listaAmplitudes = self.listaAmplitudesXML()

        #while listaSenales is not None:
        pass

    def generarGrafica(self, nombreArchivo, colorNodo): #opcion5
        grafica = Graph(nombreArchivo, colorNodo)
        temporal = self.nodoInicial
        while temporal != None:
            grafica.agregar(temporal, temporal.getSiguiente(), direccion='TB')
            temporal = temporal.getSiguiente()
        grafica.generar()
    
    def generarGraficaXML(self, nombreArchivo, colorNodo): #opcion5
        #senal = Senal()
        grafica = Graph(nombreArchivo, colorNodo)
        temporal = self.nodoInicial
        while temporal != None:
            grafica.agregar(temporal, temporal.getSiguiente(), direccion='TB')
            temporal = temporal.getSiguiente()
        grafica.generar()

    def imprimir(self): #prueba con listas
        temporal = self.nodoInicial
        while temporal != None:
            print(temporal.getDato())
            temporal = temporal.getSiguiente()


class ListaSenales:
    def __init__(self):
        self.primer = None

    def agregarSenal(self, senal):
        nuevo = NSenal(senal)
        nuevo.siguiente = self.primer
        self.primer = nuevo

    def buscarSenal(self, nombre):
        actual = self.primer
        while actual:
            if actual.senal.nombre == nombre:
                return actual.senal
            actual = actual.siguiente
        return None

class SenalNombre(): # senal
    def __init__(self, nombre):
        self.nombre = nombre
        self.primero = None
    
    def getNombre(self):
        return self.nombre

class NodoDatoComparativo():
    def __init__(self, tiempoT, amplitudA, datoD):
        self.tiempoT = tiempoT
        self.amplitudA = amplitudA
        self.datoD = datoD
        self.siguiente = None 

class SenalesReducidas():
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima, datosTiempos, amplitudA, datos):
        self.nombre = nombre
        self.tiempoMaximo = tiempoMaximo
        self.amplitudMaxima = amplitudMaxima
        self.datosTiempos = datosTiempos
        self.amplitudA = amplitudA
        self.datos = datos

class Tiempo():
    def __init__(self, tiempo):
        self.tiempo = tiempo

    def getTiempo(self):
        return self.tiempo

class TiempoAmplitud():
    def __init__(self, tiempo, amplitud):
        self.tiempo = tiempo
        self.amplitud = amplitud

    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
class NSenal:
    def __init__(self, senal):
        self.senal = senal
        self.siguiente = None
    
class NGrupo:
    def __init__(self):
        self.tiempos = NTiempo()
        self.datos = NDato()
        self.siguiente = None

class NTiempo:
    def __init__(self, tiempo=None):
        self.tiempo = tiempo
        self.siguiente = None

class NDato:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class EtiquetaDato: # dato
    def __init__(self, t, A, valor):
        self.t = t
        self.A = A
        self.valor = valor
        self.siguiente = None
