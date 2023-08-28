import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from Senal import Senal
from Cola import Cola
import copy as copyAsStr

#colores para graficasss
verde = 'green'
rosa = 'pink'
class LecturaXML():
    def __init__(self, ruta):
        self.raiz = ET.parse(ruta).getroot()
        self.cola = Cola()
        self.colaBinaria = Cola()

    def getSenal(self):
        #listaSenales = ListaSimple()
        for senal in self.raiz.findall('senal'):
            nombreSenal = senal.get('nombre')
            tiempoMaximo = senal.get('t')
            amplitudMaxima = senal.get('A')
            #temporalSenal = Senal(nombreSenal, tiempoMaximo, amplitudMaxima)

            print(nombreSenal, tiempoMaximo, amplitudMaxima)

        #return listaSenales
        
        #temporalSenal.getNombre()

        #return temporalSenal

        #print("_____Lista de senales_____")
        #senalGuardada = listaSenales.getInicial()
        #while senalGuardada != None:
            #print(senalGuardada.getDato().getNombre())
            #senalGuardada = senalGuardada.getSiguiente()
    
    def getDatos(self):
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.cola.insertar(int(dato.text))

        colaEnProceso = self.cola

        colaBinaria = copyAsStr.deepcopy(self.cola)
        colaBinaria.convertirABinario()
        colaBinaria.graficar('colaBinaria', 'red')
        self.cola.graficar('cola', verde)
        self.cola.graficar('cola2', rosa)
        self.cola.imprimir()
        #self.cola.generarSalidaXML('holagato')
        colaBinaria = copyAsStr.deepcopy(self.cola)
        colaBinaria.imprimir()
        return self.cola
    #colaEnProceso, colaBinaria

    def ordenardoDatosXMLsinprocesar(self):
        self.cola
        self.cola.imprimir()
        self.cola.graficar('cola', verde)
        self.cola.graficar('cola2', rosa)
        self.cola.imprimir()

    def getListaConvertirABinario(self):
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.cola.insertar(int(dato.text))
        self.colaBinaria = copyAsStr.deepcopy(self.cola)

        #lista de datos binarios ------------------------------------
        self.colaBinaria.convertirABinario()
        #self.colaBinaria.graficar('colaBinaria', 'red')
        #self.colaBinaria.imprimir()

        return self.colaBinaria
    
    def cargaArchivo(self):
        pass
        #self.colaBinaria.imprimir()

    def procesarSalidaBinaria(self): #opcion2
        #temporal = self.nodoInicial
        pass


    #def generarSalidaXML(self): #opcion3
        #actual = self.nodoInicial

        #xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str#('"UTF-8"') + '?>\n'
        #xml += '<senalesReducidas>\n'

        #while actual is not None:
            #xml += '    <senal nombre= "'+actual.getSenalPatron()'"'


#objLectura = LecturaXML('entrada1.xml')
#objLectura.getSenal()
#objLectura.getDatos()
#objLectura.ordenardoDatosXMLsinprocesar()