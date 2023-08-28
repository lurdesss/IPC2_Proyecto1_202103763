from ListaSimple import ListaSimple
from Tiempo import Tiempo

class Senal:
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima):
        self.nombre = nombre
        self.tiempoMaximo = tiempoMaximo
        self.amplitudMaxima = amplitudMaxima
        self.tiempos = ListaSimple()
        self.crearListaTiempo()
        self.imprimir()

    def getNombre(self):
        return self.nombre

    def getTiempoMaximo(self):
        return self.tiempoMaximo

    def getAmplitudMaxima(self):
        return self.amplitudMaxima

    def crearListaTiempo(self):
        for i in range(1, int(self.tiempoMaximo)+1):
            objetoTiempo = Tiempo(i, self.amplitudMaxima)

            #lista de tiempos
            self.tiempos.agregarAlFinal(objetoTiempo)
        return self.tiempos
    
    def imprimir(self):
        print("_____Tiempos para senal:", self.getNombre() ,"_____")
        tmpTiempo = self.tiempos.getInicial()
        while tmpTiempo != None:
            print(tmpTiempo.getDato().getTiempo())
            tmpTiempo = tmpTiempo.getSiguiente()
