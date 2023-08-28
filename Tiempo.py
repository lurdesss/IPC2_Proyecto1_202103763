from ListaSimple import ListaSimple
from Amplitud import Amplitud

class Tiempo():
    def __init__(self, tiempo, amplitud):
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.listaAmplitudes = ListaSimple()
        self.llenarListaAmplitudes()
        self.procesarPatron()
    
    def getTiempo(self):
        return self.tiempo
    
    def getAmplitud(self):
        return self.amplitud
    
    def llenarListaAmplitudes(self):
        for i in range(1, int(self.amplitud)+1):
            temporalAmplitud = Amplitud(i)
            #lista de amplitudes
            self.listaAmplitudes.agregarFinal(temporalAmplitud)
        return self.listaAmplitudes

    def imprimir(self): #prueba    -------------------------------------------------
        print("_____Amplitudes para tiempo:", self.getTiempo() ,"_____")
        objAmplitud = self.listaAmplitudes.getInicial()
        while objAmplitud != None:
            print(objAmplitud.getDato().getAmplitud())
            objAmplitud = objAmplitud.getSiguiente()

    def procesarPatron(self):
        pass