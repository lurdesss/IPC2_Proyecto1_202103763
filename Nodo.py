class Nodo():
    def __init__(self, id, dato):
    #atributos
        self.id = id
        self.dato = dato
        self.siguiente = None
    
    #getters
    def getId(self):
        return self.id
    
    def getDato(self):
        return self.dato
    
    def getSiguiente(self):
        return self.siguiente
    
    #setters
    def setId(self, id):
        self.id = id
    
    def setDato(self, dato):
        self.dato = dato

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
