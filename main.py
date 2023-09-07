import xml.etree.ElementTree as ET
from colorama import Fore, init
init()
from LecturaXML import LecturaXML
#from ListaSimple import ListaSimple

def opcionesMenu():
    print(Fore.CYAN +"\n                    MENÚ                  ")
    print(Fore.CYAN +"         1. Cargar archivo XML              ")
    print(Fore.CYAN +"         2. Procesar archivo                ")
    print(Fore.CYAN +"         3. Escribir archivo salida XML     ")
    print(Fore.CYAN +"         4. Mostrar datos del estudiante    ")
    print(Fore.CYAN +"         5. Generar gráfica                 ")
    print(Fore.CYAN +"         6. Inicializar sistema             ")
    print(Fore.CYAN +"         7. Salida                          ")

def menu():
    opcion = ""
    ruta = ""

    while opcion != "7":
        opcionesMenu()
        opcion = input(Fore.WHITE +"\n   Seleccione una opcion del menú: ")

        if opcion == "1": # Cargar archivo .xml
            try:
                nombreArchivo = input(Fore.YELLOW + "\n        Ingrese el nombre del archivo (sin extensión): ")
                ruta = nombreArchivo +".xml"
                listaSenales = LecturaXML(ruta)
                print("")
                listaSenales.cargarSenal()
                print(Fore.GREEN + "\n           Se cargó el archivo con éxito")
            except:
                print(Fore.RED + "\n      Error en carga de archivo")
        elif opcion == "2": # Procesar archivo
            try:
                print(Fore.YELLOW +"\n        Procesando archivo...                    \n")
                listaSenales.procesarArchivo()
                print(Fore.GREEN + "\n        Se ha finalizado el procesamiento de archivo "+ Fore.WHITE + ruta + "\n")
            except:
                print(Fore.RED+ "\n        Error al procesar archivo "+ Fore.WHITE + "'" + nombreArchivo + "'")
        elif opcion == "3": # Generar salida XML
            try:
                listaSenales.generarSalida()
                print(Fore.YELLOW + "        Escribiendo archivo salida...")
            except:
                print(Fore.RED+ "        No se ha podido escribir el archivo salida")
        elif opcion == "4": # Datos del estudiante
                print(Fore.WHITE +"\n       Datos del estudiante           ")
                print(Fore.WHITE +"   Jennifer Yulissa Lourdes Taperio Manuel   ")
                print(Fore.WHITE +"   202103763                                 ")
                print(Fore.WHITE +"   Introduccion a la programacion y computacion seccion \"N\"")
                print(Fore.WHITE +"   Ingeniería en ciencias y sistemas         ")
                print(Fore.WHITE +"   Sexto semestre                            ")
        elif opcion == "5": # Generar gráfica
            try:
                print(Fore.YELLOW +"        Generando gráfica...")
                listaSenales.getDatosPRUEBAS()
                print(Fore.GREEN +"        Gráfica generada con éxito")
            except:
                print("     No se ha podido generar la gráfica")
        elif opcion == "6":
            try:
                listaSenales.generarSalidaXMLxIF()
                print(Fore.YELLOW + "        Inicializando sistema...")
            except:
                print(Fore.RED + "        No se ha podido inicializar el sistema")
        elif opcion == "7":
                print(Fore.WHITE + "        Hasta pronto!                 ")
                break
menu()