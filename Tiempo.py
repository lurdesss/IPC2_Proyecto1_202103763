from ListaSimple import ListaSimple
from Amplitud import Amplitud

class Tiempo():
    def __init__(self, tiempo, amplitud):
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.lisatAmplitudes = ListaSimple()
        self.llenarListadoAmplitudes()
        self.procesarPatron()
    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def llenarListaAmplitudes(self):
        pass

    def procesarPatron(self):
        pass