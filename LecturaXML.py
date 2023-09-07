import xml.etree.ElementTree as ET
from ListaSimple import *
from Senal import *
from Tiempo import Tiempo
from Amplitud import Amplitud
import copy as copyAsStr
from colorama import Fore, init
init()
#from SenalesReducidas import SenalesReducidas

#colores para graficasss
verde = 'green'
rosa = 'pink'
class LecturaXML():
    def __init__(self, ruta):
        self.raiz = ET.parse(ruta).getroot()
        self.cola = ListaSimple()
        self.colaBinaria = ListaSimple()
        self.listaSenaless = ListaSimple()
        self.listaTiemposs = ListaSimple()
        self.listaAmplitudess = ListaSimple()
        self.senales = ListaSenales()
        self.tiempo = ListaSimple()
        self.listaTiempo = ListaSimple()
        self.listaAmplitud = ListaSimple()

    def getSenales(self):
        #listaSenaless = ListaSimple()
        for senal in self.raiz.findall('senal'):
            nombreSenal = senal.get('nombre')
            tiempoMaximo = senal.get('t')
            amplitudMaxima = senal.get('A')
            # guarda en una lista en una clase Senal
            objetoSenal = Senal(nombreSenal, tiempoMaximo, amplitudMaxima)
            self.listaSenaless.agregarAlFinal(objetoSenal)
        # retorna una lista de: nombreSenal, tiempoMaximo, amplitudMaxima
        return self.listaSenaless

    def getTiempos(self): # nodo tiempo
        for senal in self.raiz.findall('senal'):
            tiempoMaximo = senal.get('t')
            amplitudMaxima = senal.get('A')
            objetoTiempo = Tiempo(tiempoMaximo, amplitudMaxima)
            self.listaTiemposs.agregarAlFinal(objetoTiempo)
        # retorna una lista de: tiemposMaximos
        return self.listaTiemposs

    def getAmplitudes(self):
        for senal in self.raiz.findall('senal'):
            amplitudMaxima = senal.get('A')
            #dato = senal.find('dato').text
            dato = senal.find('dato').text
            objetoAmplitud = Amplitud(amplitudMaxima, dato)
            self.listaAmplitudess.agregarAlFinal(objetoAmplitud)
        # retorna una lista de: amplitudesMaximas
        return self.listaAmplitudess
    
    def getDatos(self): #nodo dato
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.cola.agregarAlFinal(int(dato.text))
            # retorna una lista de: datos
            return self.cola
    
    def getListaConvertirABinario(self): #convertir a binario y graficar
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.cola.agregarAlFinal(int(dato.text))
            self.colaBinaria = copyAsStr.deepcopy(self.cola)
            self.colaBinaria.convertirABinario()
            return self.colaBinaria

    def getDatosPRUEBAS(self):
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.cola.agregarAlFinal(int(dato.text))

        colaBinaria = copyAsStr.deepcopy(self.cola)
        colaBinaria.convertirABinario()
        colaBinaria.generarGrafica('colaBinaria', 'red')
        nombreArchivo = input("\n      Ingrese un nombre para gráfica: ")
        self.cola.generarGrafica(nombreArchivo, verde)
        self.cola.generarGrafica("cola", rosa)
    
    def cargarSenal(self): #opcion1
        for etiquetaSenal in self.raiz.findall('senal'):
            nombreSenal = etiquetaSenal.get('nombre')
            nombreSenalNueva = SenalNombre(nombreSenal)
            for etiquetaDato in etiquetaSenal.findall('dato'):
                datoT = int(etiquetaDato.get('t'))
                datoA = int(etiquetaDato.get('A'))
                valor = int(etiquetaDato.text)
                self.agregarEtiquetaSenalDato(nombreSenalNueva, datoT, datoA, valor)
            if not self.senales.buscarSenal(nombreSenal):
                self.senales.agregarSenal(nombreSenalNueva)
                print(Fore.WHITE + f"           Se ha añadido '{nombreSenal}' al sistema.")
            else:
                print(Fore.WHITE + f"\n           No se ha podido añadir '{nombreSenal}', ya ha sido añadida anteriormente.")
    
    def agregarEtiquetaSenalDato(self, senal, t, A, valor):
        nuevo = EtiquetaDato(t, A, valor)
        if not senal.primero:
            senal.primero = nuevo
        else:
            actual = senal.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def procesarArchivo(self):
        senalEnProceso = self.senales.primer
        while senalEnProceso:
            print(Fore.WHITE + f"           Se está procesando {senalEnProceso.senal.nombre}")
            senalEnProceso = senalEnProceso.siguiente
    
    def NodoTiempoAmplitudX(self):
        tiempoActual = self.getTiempos().getInicial()
        while tiempoActual is not None:
            amplitud = tiempoActual.getDato().getAmplitud()
            tiempo = tiempoActual.getDato().getTiempo()
            for i in range(1, int(tiempo)+1):
                for j in range(1, int(amplitud)+1):
                    objetoTiempo = TiempoAmplitud(i, j)
                    self.listaTiempo.agregarAlFinal(objetoTiempo)
            tiempoActual = tiempoActual.getSiguiente()
            return self.listaTiempo
    
    def NodoTiempoAmplitudx(self):
        datoActual = self.getDatos().getInicial() # lista de datos
        tiempoActual = self.getTiempos().getInicial()
        while tiempoActual and datoActual is not None:
            datoActual.getDato()
            amplitud = tiempoActual.getDato().getAmplitud()
            tiempo = tiempoActual.getDato().getTiempo()
            for i in range(1, int(tiempo)+1):
                for j in range(1, int(amplitud)+1):
                    datoActual = datoActual.getSiguiente()
                    self.dato.agregarAlFinal(datoActual)
                    objetoTiempo = TiempoAmplitud(i, self.dato)
                    self.listaTiempo.agregarAlFinal(objetoTiempo)
            tiempoActual = tiempoActual.getSiguiente()
            return self.listaTiempo

    def NodoTiempoAmplitud(self):
        tiempoActual = self.getTiempos().getInicial()
        while tiempoActual is not None:
            amplitud = tiempoActual.getDato().getAmplitud()
            tiempo = tiempoActual.getDato().getTiempo()
            for i in range(1, int(tiempo)+1):
                for j in range(1, int(amplitud)+1):
                    objetoTiempo = TiempoAmplitud(i, j)
                    self.listaTiempo.agregarAlFinal(objetoTiempo)
            tiempoActual = tiempoActual.getSiguiente()
            return self.listaTiempo


    def crearGrupos(self, senal):
        ultimoGrupo = NGrupo()
        datoActual = senal.primero
        while datoActual:
            if not ultimoGrupo.tiempos.tiempo: 
                nuevoTiempo = NTiempo(datoActual.t)
                ultimoGrupo.tiempos = nuevoTiempo
                ultimoGrupo.datos = NDato(datoActual)
            else:
                ultimoTiempo = ultimoGrupo.tiempos
                while ultimoTiempo.siguiente:
                    ultimoTiempo = ultimoTiempo.siguiente
                if datoActual.t - ultimoTiempo.tiempo == 1:
                    nuevoTiempo = NTiempo(datoActual.t)
                    ultimoTiempo.siguiente = nuevoTiempo
                else:
                    nuevoGrupo = NGrupo()
                    nuevoGrupo.tiempos = NTiempo(datoActual.t)
                    nuevoGrupo.datos = NDato(datoActual)
                    ultimoGrupo.siguiente = nuevoGrupo
                    ultimoGrupo = nuevoGrupo
                ultimoDato = ultimoGrupo.datos
                while ultimoDato.siguiente:
                    ultimoDato = ultimoDato.siguiente
                ultimoDato.siguiente = NDato(datoActual)
            datoActual = datoActual.siguiente
        return ultimoGrupo
        

    def amplitudesssX(self):
        amplitudActual = self.getTiempos().getInicial()
        while amplitudActual is not None:
            amplitud = amplitudActual.getDato().getAmplitud()
            for i in range(1, int(amplitud)+1):
                objetoTiempo = TiempoAmplitud(i, amplitud)
                self.listaAmplitud.agregarAlFinal(objetoTiempo)
            amplitudActual = amplitudActual.getSiguiente()
            return self.listaAmplitud
        
    def dividirEnGrupos(self):
        listaTiempo = ListaSimple()
        senalActual = self.getSenal().getInicial() # nombre, Tmax, Amax
        tiempoActual = self.getTiempos().getInicial() # Tmax, Amax
        amplitudActual = self.getAmplitudes().getInicial() # Amax, dato Inicial de cada senal
        binarioActual = self.getDatosEnBinario().getInicial() # lista de datos en binario

        while senalActual is not None:
            senal = senalActual.getDato().getNombre()
            amplitud = senalActual.getDato().getAmplitud()
            tiempo = senalActual.getDato().getTiempo()
            datoActual = self.getDatos().getInicial() # lista de datos
            #t =1
            for t in range(1, int(tiempo)+1):
                objetoTiempo = TiempoAmplitud(t, tiempo)
                listaTiempo.agregarAlFinal(objetoTiempo)
    
    def crearGruposNoBinarios(self):
        senalActual = self.getSenal().getInicial() # nombre, Tmax, Amax
        while senalActual is not None:
            senal = senalActual.getDato().getNombre()
            amplitud = senalActual.getDato().getAmplitudMaxima()
            datoActual = self.getDatos().getInicial() # lista de datos
            tiempo = self.tiempoEtiqueta().getInicial() # lista de tiempos
            while tiempo and datoActual is not None:
                tmp = tiempo.getDato().getTiempo()
                for i in range(1, int(amplitud)+1):
                    datoActual.getDato()
                    datoActual = datoActual.getSiguiente()

    def crearGruposBinarios(self):
        binarioActual = self.getDatosEnBinario().getInicial() # lista de datos en binario
        senalActual = self.getSenal().getInicial() # nombre, Tmax, Amax

    def tiempoEtiqueta(self):
        tiempoActual = self.getTiempos().getInicial()
        while tiempoActual is not None:
            tiempo = tiempoActual.getDato().getTiempo()
            for i in range(1, int(tiempo)+1):
                objetoTiempo = Tiempo(i)
                self.listaTiempo.agregarAlFinal(objetoTiempo)
            tiempoActual = tiempoActual.getSiguiente()
            return self.listaTiempo

    def NodoSenal(self):
        for senal in self.raiz.findall('senal'):
            nombreSenal = senal.get('nombre')
            tiempoMaximo = senal.get('t')
            amplitudMaxima = senal.get('A')
            # guarda en una lista en una clase Senal
            objetoSenal = Senal(nombreSenal, tiempoMaximo, amplitudMaxima)
            self.listaSenaless.agregarAlFinal(objetoSenal)
        # retorna una lista de: nombreSenal, tiempoMaximo, amplitudMaxima
        return self.listaSenaless
    
    def NodoGrupo(self):
        etiquetaTiempo = self.tiempoEtiqueta().getInicial()
        amplitudMaxima = self.getSenales().getInicial()
        while etiquetaTiempo and amplitudMaxima is not None:
            tiempo = etiquetaTiempo.getDato().getTiempo()
            amplitud = amplitudMaxima.getDato().getAmplitudMaxima()
            while tiempo <= int(amplitud):

                etiquetaTiempo = etiquetaTiempo.getSiguiente()

                
    def amplitudMaximaXML(self, senal):
        ampMaxima = 0 # donde A es amplitud maxima A del documento xml
        datoAmplitud = senal.primero
        while datoAmplitud:
            if datoAmplitud.A > ampMaxima:
                ampMaxima = datoAmplitud.A
            datoAmplitud = datoAmplitud.siguiente
        return ampMaxima
    

    def generarSalidaXML(self): #opcion3
        nombreArchivo = input(Fore.YELLOW + "\n      Ingrese el nombre del archivo salida (sin extensión): ")
        xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n'
        xml += '<senalesReducidas>\n'

        senalActual = self.senales.primer
        while senalActual:
            senal = senalActual.senal
            xml += f'   <senal nombre="{senal.nombre}" A="{self.amplitudMaxima(senal)}">\n'
            grupoActual = self.crearGrupos(senal)
            g =1
            while grupoActual:
                xml += f'      <grupo g="{g}">\n'
                xml += f'         <tiempos>'
                tiempoActual =  grupoActual.tiempos
                condicion = True
                while tiempoActual:
                    if not condicion:
                        xml += ','
                    else:
                        condicion = False
                    tmp = str(tiempoActual.tiempo)
                    #xml += '' + (str(tiempoActual.tiempo)) + ''
                    xml += f'{tmp}'
                    tiempoActual = tiempoActual.siguiente
                xml += '</tiempos>\n'
                xml += f'         <datosGrupo>\n'
                datoCorrespondido = grupoActual.datos
                A =1
                while datoCorrespondido:
                    datox = datoCorrespondido.dato.valor
                    xml += f'            <dato A="{A}">' + {datox} + '</dato>\n'
                    datoCorrespondido = datoCorrespondido.siguiente
                    A +=1
                xml += f'         </datosGrupo>\n'
                xml += f'         </tiempos>\n'
                xml += f'      </grupo>\n'
                grupoActual = grupoActual.siguiente
                g +=1
            xml += f'   </senal>\n'
            senalActual = senalActual.siguiente
        
        xml += '</senalesReducidas>'
        ruta = "archivos/" + nombreArchivo +".xml"
        # ruta = nombreArchivo
        with open(ruta, 'w') as documentoBinario:
            documentoBinario.write(xml)


    def generarSalida(self):
        nombreArchivo = input(Fore.YELLOW + "        Nombre del archivo de salida con extension .xml: ")
        ruta = nombreArchivo

        with open(ruta, "w") as salida:
            salida.write('<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n')
            salida.write('<senalesReducidas>\n')
            senalActual = self.senales.primer
            while senalActual:
                etiquetaSenal = senalActual.senal
                salida.write(f'   <senal nombre="{etiquetaSenal.nombre}" A="{self.amplitudMaximaXML(etiquetaSenal)}">\n')
                grupoActual = self.crearGrupos(etiquetaSenal)
                g = 1
                while grupoActual:
                    salida.write(f'      <grupo g={g}>\n')
                    salida.write('         <tiempos>')
                    tiempoCorrespondido = grupoActual.tiempos
                    primero = True
                    while tiempoCorrespondido:
                        if not primero:
                            salida.write(',')
                        else:
                            primero = False
                        salida.write(str(tiempoCorrespondido.tiempo))
                        tiempoCorrespondido = tiempoCorrespondido.siguiente
                    salida.write('</tiempos>\n')
                    salida.write('         <datosGrupo>\n')
                    datoCorrespondido = grupoActual.datos
                    A = 1
                    while datoCorrespondido:
                        salida.write(f'            <dato A={A}>{datoCorrespondido.dato.valor}</dato>\n')
                        datoCorrespondido = datoCorrespondido.siguiente
                        A +=1
                    salida.write('         </datosGrupo>\n')
                    salida.write('      </grupo>\n')
                    grupoActual = grupoActual.siguiente
                    g += 1
                salida.write('   </senal>\n')
                senalActual = senalActual.siguiente
            salida.write('</senalesReducidas>\n')

### funcional 

    def generarSalidaXMLx(self): #opcion3
        nombreArchivo = input(Fore.YELLOW + "\n      Ingrese el nombre del archivo salida (sin extensión): ")
        xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n'
        xml += '<senalesReducidas>\n'

        senalActual = self.senales.nodoInicial
        while senalActual:
            nombreSenal = senalActual.senal
            xml += f'   <senal nombre="{nombreSenal}" A="{self.amplitudMaxima(nombreSenal)}">\n'
            grupoActual = self.crearGrupos(senalActual)
            g =1
            while grupoActual:
                xml += f'      <grupo g="{g}">\n'
                xml += f'         <tiempos>'
                tiempoCorrespondido =  grupoActual.tiempos
                condicion = True
                while tiempoCorrespondido:
                    if not condicion:
                        xml += ','
                    else:
                        condicion = False
                    xml += str(tiempoCorrespondido.tiempo)
                    tiempoCorrespondido = tiempoCorrespondido.siguiente
                xml += '</tiempos>\n'
                xml += f'         <datosGrupo>\n'
                datoCorrespondido = grupoActual.datos
                A =1
                while datoCorrespondido:
                    xml += f'            <dato A="{A}">{datoCorrespondido.dato.dato}</dato>\n'
                    datoCorrespondido = datoCorrespondido.siguiente
                    A +=1
                xml += f'         </datosGrupo>\n'
                xml += f'         </tiempos>\n'
                xml += f'      </grupo>\n'
                grupoActual = grupoActual.siguiente
                g +=1
            xml += f'   </senal>\n'
            senalActual = senalActual.siguiente
        
        xml += '</senalesReducidas>'
        ruta = "archivos/" + nombreArchivo +".xml"
        # ruta = nombreArchivo
        with open(ruta, 'w') as documentoBinario:
            documentoBinario.write(xml)

    def generarSalidaXMLxIFy(self): #opcion3
        nombreArchivo = input(Fore.YELLOW + "\n      Ingrese el nombre del archivo salida (sin extensión): ")
        xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n'
        #xml += '<senalesReducidas>\n'

        soloSenal = self.senalesCargadas().getInicial()
        senalActual = self.getSenales().getInicial()
        senalS = soloSenal.getDato().getNombre()
        nombreS = senalActual.getDato().getNombre()
        while soloSenal is not None and senalS == nombreS:
            xml += '<senalesReducidas>\n'
            while senalActual is not None:
                #xml += '<senalesReducidas>\n'
                nombreSenal = senalActual.getDato().getAmplitudMaxima()
                amplitudMaxima = senalActual.getDato().getNombre()
                xml += f'   <senal nombre="{nombreSenal}" A="{amplitudMaxima}">\n'
                grupoActual = self.getTiempos().getInicial()
                nombreSenalGrupo = grupoActual.getDato().getAmplitud()
                g =1
                while grupoActual is not None and (nombreSenal == nombreSenalGrupo):
                    tiempoCorrespondido =  grupoActual.getDato().getTiempo()
                    xml += f'      <grupo g="{g}">\n'
                    xml += f'         <tiempos>' + tiempoCorrespondido + ' </tiempos>\n'
                    xml += f'         <datosGrupo>\n'
                    datoCorrespondido = self.getAmplitudes().getInicial()
                    nombreSenalDatoCorrespondido = datoCorrespondido.getDato().getAmplitud()
                    A =1
                    while datoCorrespondido is not None and (nombreSenal == nombreSenalDatoCorrespondido):
                        dato = datoCorrespondido.getDato().getAmplitud()
                        xml += f'            <dato A="{A}">' + dato + '</dato>\n'
                        datoCorrespondido = datoCorrespondido.getSiguiente()
                        A +=1
                    xml += f'         </datosGrupo>\n'
                    xml += f'         </tiempos>\n'
                    xml += f'      </grupo>\n'
                    grupoActual = grupoActual.getSiguiente()
                    g +=1
                xml += f'   </senal>\n'
                #xml += '</senalesReducidas>\n'
                senalActual = senalActual.getSiguiente()
            soloSenal = soloSenal.getSiguiente()
            xml += '</senalesReducidas>\n'
            #soloSenal = soloSenal.getSiguiente()
            #xml += '</senalesReducidas>'
            #senalActual = senalActual.getSiguiente()
            #soloSenal = soloSenal.getSiguiente()
        #xml += '</senalesReducidas>'
        #documento = ruta + '.xml'
        ruta = "archivos/" + nombreArchivo +".xml"
        with open(ruta, 'w') as documentoBinario:
            documentoBinario.write(xml)

### funcional

    def generarSalidaXMLxIF(self): #opcion3
        nombreArchivo = input(Fore.YELLOW + "\n      Ingrese el nombre del archivo salida (sin extensión): ")
        xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n'
        xml += '<senalesReducidas>\n'
        senalActual = self.getSenales().getInicial()
        while senalActual is not None:
            amplitudMaxima = senalActual.getDato().getNombre()
            nombreSenal = senalActual.getDato().getAmplitudMaxima()
            xml += f'   <senal nombre="{nombreSenal}" A="{amplitudMaxima}">\n'
            grupoActual = self.getTiempos().getInicial()
            nombreSenalGrupo = grupoActual.getDato().getAmplitud()
            if nombreSenal == nombreSenalGrupo:
                g =1
                while grupoActual is not None:
                    tiempoCorrespondido =  grupoActual.getDato().getTiempo()
                    xml += f'      <grupo g="{g}">\n'
                    xml += f'         <tiempos>' + tiempoCorrespondido + ' </tiempos>\n'
                    xml += f'         <datosGrupo>\n'
                    datoCorrespondido = self.getAmplitudes().getInicial()
                    nombreSenalDatoCorrespondido = datoCorrespondido.getDato().getAmplitud()
                    if nombreSenal == nombreSenalDatoCorrespondido:
                        A =1
                        while datoCorrespondido is not None:
                            dato = datoCorrespondido.getDato().getAmplitud()
                            xml += f'            <dato A="{A}">' + dato + '</dato>\n'
                            datoCorrespondido = datoCorrespondido.getSiguiente()
                            A +=1
                    xml += f'         </datosGrupo>\n'
                    xml += f'         </tiempos>\n'
                    xml += f'      </grupo>\n'
                    grupoActual = grupoActual.getSiguiente()
                    g +=1
            else:
                xml += f'   </senal>\n'
            senalActual = senalActual.getSiguiente()
        
        xml += '</senalesReducidas>'
        #documento = ruta + '.xml'
        ruta = "archivos/" + nombreArchivo +".xml"
        #ruta = nombreArchivo
        with open(ruta, 'w') as documentoBinario:
            documentoBinario.write(xml)


    def generarSalidaXMLxIFK(self): #opcion3
        nombreArchivo = input(Fore.YELLOW + "\n      Ingrese el nombre del archivo salida (sin extensión): ")
        xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n'
        #xml += '<senalesReducidas>\n'
        xml += '<senalesReducidas>\n'

        soloSenal = self.senalesCargadas().getInicial()
        senalActual = self.getSenales().getInicial()
        senalS = soloSenal.getDato().getNombre()
        nombreS = senalActual.getDato().getNombre()
        while soloSenal is not None and senalS == nombreS:
            while senalActual is not None:
                nombreSenal = senalActual.getDato().getAmplitudMaxima()
                amplitudMaxima = senalActual.getDato().getNombre()
                xml += f'   <senal nombre="{nombreSenal}" A="{amplitudMaxima}">\n'
                grupoActual = self.getTiempos().getInicial()
                nombreSenalGrupo = grupoActual.getDato().getAmplitud()
                g =1
                while grupoActual is not None and (nombreSenal == nombreSenalGrupo):
                    tiempoCorrespondido =  grupoActual.getDato().getTiempo()
                    xml += f'      <grupo g="{g}">\n'
                    xml += f'         <tiempos>' + tiempoCorrespondido + ' </tiempos>\n'
                    xml += f'         <datosGrupo>\n'
                    datoCorrespondido = self.getAmplitudes().getInicial()
                    nombreSenalDatoCorrespondido = datoCorrespondido.getDato().getAmplitud()
                    A =1
                    while datoCorrespondido is not None and (nombreSenal == nombreSenalDatoCorrespondido):
                        dato = datoCorrespondido.getDato().getAmplitud()
                        xml += f'            <dato A="{A}">' + dato + '</dato>\n'
                        datoCorrespondido = datoCorrespondido.getSiguiente()
                        A +=1
                    xml += f'         </datosGrupo>\n'
                    xml += f'         </tiempos>\n'
                    xml += f'      </grupo>\n'
                    grupoActual = grupoActual.getSiguiente()
                    g +=1
                xml += f'   </senal>\n'
                xml += '</senalesReducidas>'
                senalActual = senalActual.getSiguiente()
            soloSenal = soloSenal.getSiguiente()
        ruta = "archivos/" + nombreArchivo +".xml"
        with open(ruta, 'w') as documentoBinario:
            documentoBinario.write(xml)

    def tiemposss(self):
        senalActual = self.getSenal().getInicial() # nombre, Tmax, Amax
        while senalActual is not None:
            tiempo = senalActual.getDato().getTiempoMaximo()
            #tiempos = senalActual.getDato().getTiempoMaximo()
            for i in range(1, int(tiempo)+1):
                objetoTiempo = TiempoAmplitud(i, tiempo)
                self.listaTiempo.agregarAlFinal(objetoTiempo)
            senalActual = senalActual.getSiguiente()
        return self.listaTiempo
    
    def getDatosOTRAPRUEBA(self):
        for senal in self.raiz.findall('senal'):
            nombreSenal = senal.get('nombre')
            tiempoMaximo = senal.get('t')
            amplitudMaxima = senal.get('A')
            objetoSenal = Senal(nombreSenal, tiempoMaximo, amplitudMaxima)
            self.listaSenaless.agregarAlFinal(objetoSenal)
            senalGuardada = self.listaSenaless.getInicial()
        while senalGuardada != None:
            for dato in senal.findall('dato'):
                self.cola.agregarAlFinal(int(dato.text))
