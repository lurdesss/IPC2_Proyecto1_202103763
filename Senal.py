class Senal():
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima):
        self.nombre = nombre
        self.tiempoMaximo = tiempoMaximo
        self.amplitudMaxima = amplitudMaxima

    def getNombre(self):
        return self.nombre

    def getTiempoMaximo(self):
        return self.tiempoMaximo

    def getAmplitudMaxima(self):
        return self.amplitudMaxima
    
class Grupo():
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo
    
    def getNombre(self):
        return self.nombre
    def getTiempo(self):
        return self.tiempo
    
class DatoSumado():
    def __init__(self, nombre, dato):
        self.nombre = nombre
        self.dato = dato
    
    def getNombre(self):
        return self.nombre
    def getDatoCorrespondido(self):
        return self.dato


