import graphviz

class Graph():
    def __init__(self, nombreArchivo, colorNodo):
        self.nombreArchivo = nombreArchivo
        self.colorNodo = colorNodo
        self.dot = graphviz.Digraph('structs', filename=f'{self.nombreArchivo}.gv', node_attr={'shape':'egg' ,'color': f'{self.colorNodo}', 'style': 'filled', 'fontname': 'Helvetica'})
        
    def agregar(self, nodoInicial, nodoSiguiente, direccion):
        if(nodoSiguiente != None):
            self.dot.node(str(nodoInicial.getId()), str(nodoInicial.getDato()))
            self.dot.node(str(nodoSiguiente.getId()), str(nodoSiguiente.getDato()))
            self.dot.edge(str(nodoInicial.getId()), str(nodoSiguiente.getId()))
            self.dot.attr(rankdir=direccion)

    def agregarElementosAnidados(self, nombreSenal, tiempo, amplitud, dimensionAmplitudes, direccion="TB"):
        if(dimensionAmplitudes != None):
            self.dot.node(nombreSenal,str(nombreSenal.getNombre()))
            self.dot.node(tiempo,str(tiempo.getTiempo()))
            self.dot.node(amplitud, str(amplitud.getAmplitud()))
            self.dot.node(dimensionAmplitudes, str(dimensionAmplitudes.getDimensionAmplitudes()))
            self.dot.edge(nombreSenal,tiempo)
            self.dot.edge(nombreSenal,amplitud)
            self.dot.edge(nombreSenal,dimensionAmplitudes)
            self.dot.attr(rankdir=direccion)
    
    def generar(self):
        self.dot.render(outfile=f'files/{self.nombreArchivo}.png').replace('\\', '/')
        f'files/{self.nombreArchivo}.png'