import xml.etree.ElementTree as ET
from colorama import Fore
from LecturaXML import LecturaXML
from Tiempo import Tiempo
from Senal import Senal

def topAndBottom():
    print(Fore.WHITE +"-")

def lateral():
    print(Fore.WHITE +"|")

def opcionesMenu():
    print(Fore.CYAN +"\n    ----------------- MENÚ ----------------- ")
    print(Fore.CYAN +"   |     1. Cargar archivo XML              |")
    print(Fore.CYAN +"   |     2. Procesar archivo                |")
    print(Fore.CYAN +"   |     3. Escribir archivo salida XML     |")
    print(Fore.CYAN +"   |     4. Mostrar datos del estudiante    |")
    print(Fore.CYAN +"   |     5. Generar gráfica                 |")
    print(Fore.CYAN +"   |     6. Inicializar sistema             |")
    print(Fore.CYAN +"   |     7. Salida                          |")
    print(Fore.CYAN +"    ---------------------------------------- ")

def menu():
    opcion = ""
    ruta = ""

    while opcion != "7":
        opcionesMenu()
        opcion = input(Fore.CYAN +"\nSeleccione una opcion del menú: ")

        if opcion == "1": # Cargar archivo .xml
            try:
                nombreArchivo = input(Fore.YELLOW + "\n Ingrese el nombre del archivo: ")
                ruta = nombreArchivo +".xml"
                listaSenales = LecturaXML(ruta)
                print(Fore.GREEN + "     -------------------------------")
                print(Fore.GREEN + "   | Se cargó el archivo con éxito! |")
                print(Fore.GREEN + "     -------------------------------\n")
            except:
                print(Fore.RED + "    ---------------------------------")
                print(Fore.RED + "   |    ERROR: Datos no cargados     |")
                print(Fore.RED + "    ---------------------------------\n")
        elif opcion == "2":
            try:
                print(Fore.YELLOW +"\n         Procesando archivo...                    ")
                #listaSenales.getListaConvertirABinario().imprimir()
                #listaSenales.ordenardoDatosXMLsinprocesar()
                #listaSenales.cargaArchivo()
                #listaSenales.getSenal()
                # no listaSenales.llenarListaAmplitudes()


                print(Fore.GREEN + "    Se ha procesado el archivo "+ Fore.WHITE + ruta)
                
            except:
                print("   ------------------------------------------")
        
        elif opcion == "3":
            try:
                print("         Escribir archivo salida             ")
            except:
                print("   ------------------------------------------")
        
        elif opcion == "4":
                print(Fore.WHITE +"\n             Datos del estudiante           ")
                print(Fore.GREEN +"   > Jennifer Yulissa Lourdes Taperio Manuel   ")
                print(Fore.GREEN +"   > 202103763                                 ")
                print(Fore.GREEN +"   > Introduccion a la programacion y computacion seccion \"N\"")
                print(Fore.GREEN +"   > Ingenieria en ciencias y sistemas         ")
                print(Fore.GREEN +"   > Sexto semestre                            ")

        elif opcion == "5":
            try:
                print("         Generar gráfica                     ")
            except:
                print("   ------------------------------------------")
        
        elif opcion == "6":
            try:
                print("         Inicializar sistema                 ")
            except:
                print("   ------------------------------------------")

        elif opcion == "7":
                print("         Hasta pronto!                 ")
                break
menu()