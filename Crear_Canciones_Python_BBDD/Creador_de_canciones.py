#-*- coding: utf-8 -*-
"""
 Gestiona la creacion,borrado y visualización de las canciones de una BBDD
 Autor: Javier Ponferrada López

"""
from Cancion import Cancion
import MySQLdb


def crearCancion():
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

def mostrarCanciones():
    conn = MySQLdb.connect("127.0.0.1","root","","CANCIONES")

    cursor = conn.cursor()

    num_tuplas = cursor.execute("SELECT * FROM CANCIONES")
    for x in range(num_tuplas):
        resultado  = cursor.fetchone()
        print resultado

    conn.commit()
    conn.close()
def borrarCancion():
    mostrarCanciones()
    codigoCancion = int(raw_input("Codigo de cancion a borrar: "))
    conn = MySQLdb.connect("127.0.0.1","root","","CANCIONES")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM CANCIONES WHERE COD ='%s' " % codigoCancion)
    conn.commit()
    conn.close()

def imprimirOpcionesMenu():
    opciones = "--MENU--\n"
    opciones += "1- Crear nueva cancion.\n"
    opciones += "2- Mostrar canciones.\n"
    opciones += "3- Borrar cancion.\n"
    opciones += "4- Salir."
    print opciones

def gestionarOpcionesMenu(opcion):
    if opcion== 1:
        try:
            crearCancion()
        except:
            print "Error:al crear una nuva cancion."
    elif opcion == 2:
        mostrarCanciones()
    elif opcion == 3:
        try:
            borrarCancion()
        except:
            print "Error: al borrar la cancion."

def solicitarOpcionesMenu():
    while True:
        imprimirOpcionesMenu()
        opcion = int (raw_input("Opcion: "))
        gestionarOpcionesMenu(opcion)
        if(opcion == 4):
            break


solicitarOpcionesMenu()
