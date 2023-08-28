from ListaSimple import  ListaSimple

class Cola(ListaSimple): # Herencia

    def insertar(self, dato):
        ListaSimple.agregarAlFinal(self, dato)
    
    def imprimir(self):
        ListaSimple.imprimir(self)

    def graficar(self, nombreArchivo, colorNodo):
        ListaSimple.generarGrafica(self, nombreArchivo, colorNodo)
    
    def convertirABinario(self):
        ListaSimple.convertirABinario(self)