import graphviz

class Graph():
    def __init__(self, nombreArchivo, colorNodo):
        self.nombreArchivo = nombreArchivo
        self.colorNodo = colorNodo
        self.dot = graphviz.Digraph('structs', filename=f'{self.nombreArchivo}.gv', node_attr={'shape':'egg' ,'color': f'{self.colorNodo}', 'style': 'filled', 'fontname': 'Helvetica'})
        
    def agregar(self, nodoInicial, nodoSiguiente):
        if(nodoSiguiente != None):
            self.dot.node(str(nodoInicial.getId()), str(nodoInicial.getDato()))
            self.dot.node(str(nodoSiguiente.getId()), str(nodoSiguiente.getDato()))
            self.dot.edge(str(nodoInicial.getId()), str(nodoSiguiente.getId()))

    def agregarElementosAnidados(self):
        pass
    
    def generar(self):
        self.dot.render(outfile=f'files/{self.nombreArchivo}.png').replace('\\', '/')
        f'files/{self.nombreArchivo}.png'