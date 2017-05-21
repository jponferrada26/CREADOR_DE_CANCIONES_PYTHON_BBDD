#-*-coding: utf8-*-

"""
    Canción
"""

class Cancion(object):
    def __init__(self,titulo,autor,codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo


    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getCodigo(self):
        return self.codigo
    def setTitulo(self,titulo):
        self.titulo = titulo

    def setAutor(self,autor):
        self.autor = autor

    def mostrarCancion(self):
        cadena = "---CANCION---\n"
        cadena += "Titulo: "+self.titulo+"\n"
        cadena += "Autor: "+self.autor+"\n"
        return cadena

