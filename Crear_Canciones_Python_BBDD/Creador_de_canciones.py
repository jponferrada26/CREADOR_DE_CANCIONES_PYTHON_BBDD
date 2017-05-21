#-*- coding: utf-8 -*-
"""
 Gestiona la creacion,borrado y visualización de las canciones de una BBDD
 Autor: Javier Ponferrada López

"""
from Cancion import Cancion
import MySQLdb

#Crear una nueva cancion e inserta dicha canción en la BBDD
def crearCancionBBDD():
    new_cancion = Cancion(str(raw_input("Titulo: ")),str(raw_input("Autor: ")),int(raw_input("Codigo cancion:")))
    titulo = new_cancion.getTitulo()
    autor = new_cancion.getAutor()
    codigo = new_cancion.getCodigo()
    conn = MySQLdb.connect("127.0.0.1","root","","CANCIONES")

    cursor = conn.cursor()
    cursor.execute(("INSERT INTO CANCIONES(COD,TITULO,AUTOR) VALUES('%d','%s','%s')") %
                   (codigo,titulo,autor))
    conn.commit()
    conn.close()

#Mostrar las canciones de la BBDD
def mostrarCancionesBBDD():
    conn = MySQLdb.connect("127.0.0.1","root","","CANCIONES")

    cursor = conn.cursor()

    num_tuplas = cursor.execute("SELECT * FROM CANCIONES")
    for x in range(num_tuplas):
        resultado  = cursor.fetchone()
        print resultado

    conn.commit()
    conn.close()

#Borrar una cancion de la BBDD
def borrarCancionBBDD():
    mostrarCancionesBBDD()
    codigoCancion = int(raw_input("Codigo de cancion a borrar: "))
    conn = MySQLdb.connect("127.0.0.1","root","","CANCIONES")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM CANCIONES WHERE COD ='%s' " % codigoCancion)
    conn.commit()
    conn.close()

#Imprimir opciones del menu BBDD
def imprimirOpcionesMenuBBDD():
    opciones = "--MENU-BBDD--\n"
    opciones += "1- Crear nueva cancion.\n"
    opciones += "2- Mostrar canciones.\n"
    opciones += "3- Borrar cancion.\n"
    opciones += "4- Salir."
    print opciones

#Gestiona la opcion BBDD seleccionada por el usuario
def gestionarOpcionesMenuBBDD(opcion):
    if opcion== 1:
        try:
            crearCancionBBDD()
        except:
            print "Error:al crear una nuva cancion."
    elif opcion == 2:
        mostrarCancionesBBDD()
    elif opcion == 3:
        try:
            borrarCancionBBDD()
        except:
           print "Error: al borrar la cancion."

#Solicitar al usuario las opcion del menu BBDD
def solicitarOpcionesMenuBBDD():
    while True:
        try:
            imprimirOpcionesMenuBBDD()
            opcion = int (raw_input("Opcion: "))
            gestionarOpcionesMenuBBDD(opcion)
            if(opcion == 4):
                break
        except:
            print "Opcion incorrecta."

#Escribir una nueva cancion en un fichero de texto
def escribirNuevaCancionFichero():
    fichero = open("canciones.txt",'a')
    new_cancion = Cancion(str(raw_input("Titulo: ")),str(raw_input("Autor: ")),int(raw_input("Codigo cancion:")))
    titulo = new_cancion.getTitulo()
    autor = new_cancion.getAutor()
    codigo = str(new_cancion.getCodigo())
    fichero.write(codigo+", "+titulo+", "+autor+"\n")
    fichero.close()

#Leer todas las canciones del fichero de texto
def leerCanciones():
    fichero = open("canciones.txt",'r')
    print fichero.read()
    fichero.close()

#Vaciar todos los datos que contiene el arhivos de texto
def vaciarArchivo():
     fichero = open("canciones.txt",'w')
     fichero.write("")
     fichero.close()

#Imprimir las opciones del menu de ficheros
def imprimirOpcionesMenuFichero():
    opciones = "--MENU-FICHERO--\n"
    opciones += "1- Escribir nueva cancion.\n"
    opciones += "2- Leer canciones.\n"
    opciones += "3- Borrar contenido fichero.\n"
    opciones += "4- Salir."
    print opciones

#Gestionar las opciones del menu de ficheros
def gestionarOpcionesMenuFichero(opcion):
    if opcion== 1:
        try:
            escribirNuevaCancionFichero()
        except:
            print "Error al escribir el fichero."
    elif opcion == 2:
       leerCanciones()
    elif opcion == 3:
       vaciarArchivo()

#Solicitar las opciones del menu de ficheros
def solicitarOpcionesMenuFichero():
    while True:
        try:
            imprimirOpcionesMenuFichero()
            opcion = int (raw_input("Opcion: "))
            gestionarOpcionesMenuFichero(opcion)
            if(opcion == 4):
                break
        except:
            print "Opcion incorrecta."


#Imprimir las opciones del menu general
def imprimirOpcionesMenuGeneral():
    opciones = "--MENU-GENERAL--\n"
    opciones += "1- Base de datos.\n"
    opciones += "2- Fichero.\n"
    opciones += "3- Salir."
    print opciones

#Gestionar las opciones del menu general
def gestionarOpcionesMenuGeneral(opcion):
    if opcion== 1:
        solicitarOpcionesMenuBBDD()
    elif opcion == 2:
        solicitarOpcionesMenuFichero()

#Solicita al usuario la opcion que desee del menu general
def solicitarOpcionesGeneral():
    while True:
        try:
            imprimirOpcionesMenuGeneral()
            opcion = int (raw_input("Opcion: "))
            gestionarOpcionesMenuGeneral(opcion)
            if(opcion == 3):
                break
        except:
            print "Opcion incorrecta."

solicitarOpcionesGeneral()
