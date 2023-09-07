from Tiempo import Tiempo
from Amplitud import Amplitud
from Senal import Senal
from ListaSimple import ListaSimple

# Senales reducidas esta en donde para fila t N1 ? otra fila t N2 igual
# lo que significa que para columna A N1 ? otra columna A N2 igual
# Tambien para t N1 ? t N2 exista A N1 ? A N2 ? A N3 iguales 
# suponiendo t1 And t2 son iguales SUMAMOS las amplitudes A1 And A1
#   senal nombre A
#       grupo g
#           tiempos ###<dato>
#           datosGrupo
#                dato A ###<dato>

class SenalesReducidas():
    def __init__(self, nombre, tiempoMaximo, amplitudMaxima, datosTiempos, amplitudA, datos):
        self.nombre = nombre
        self.tiempoMaximo = tiempoMaximo
        self.amplitudMaxima = amplitudMaxima
        self.datosTiempos = datosTiempos
        self.amplitudA = amplitudA
        self.datos = datos

        #nombre es nombre senal de Senal() nombre
        #amplitud viene de Tiempo() A
        #grupo de procesarSenal en Listasimple() o aca g
        #dato de procesarSenal en Listasimple() o aca dato
        #self.senales = Senal()
        #self.tiempos = Tiempo()
        #self.amplitudes = Amplitud()

    def getNombre(self):
        return self.nombre
    
    def getTiempoMaximo(self): #para crear grupos
        return self.tiempoMaximo

    def getAmplitudMaxima(self):
        return self.amplitudMaxima
    
    def getDatosTiempos(self):
        return self.datosTiempos
    
    def getAmplitudA(self):
        return self.amplitudA
    
    def getDatos(self):
        return self.datos
    
    # setters
    def setNombre(self, nombre):
        self.nombre =nombre

    def setTiempoMaximo(self, tiempoMaximo):
        self.tiempoMaximo = tiempoMaximo
    
    def setAmplitudMaxima(self, amplitudMaxima):
        self.amplitudMaxima = amplitudMaxima
    
    def setDatosTiempos(self, datosTiempos):
        self.datosTiempos = datosTiempos

    def setAmplitudA(self, amplitudA):
        self.amplitudA = amplitudA
    
    def setDatos(self, datos):
        self.datos = datos
    