# -*- coding: utf-8 -*-

from Diccionario import Diccionario
from Texto import Texto
from Funciones import binarySearchDicc
from Funciones import normalizar

class ComparadorCustomStems():
    def __init__(self,diccionario,texto):
        self.__texto = stemArray(texto)
        self.__diccionario = stemArray(diccionario)
        self.__lista = []

    def coincidencias(self):
        for indice in range(len(self.__texto)):
            binarySearchDicc(self.__texto, indice, self.__diccionario, self.__lista, comparador)


    def getMatches(self):
        self.__lista = list(set(self.__lista))
        self.__lista.sort()
        return self.__lista
        
    def nombre(self):
        return "Comparador de stems personalizado"

    def getStemsText(self):
        return self.__texto

    def getStemsDict(self):
        return self.__diccionario

# texto vs diccionario
def comparador(string1, string2):
    return string1.startswith(string2)

#entrega la lista original con las palabras recortadas según las reglas en el
#stemmer
def stemArray(words):
    lista = []
    for word in words:
        palabras = word.split()
        termino = ""
        for palabra in palabras:
            termino += normalizar(palabra) + " "
        termino = termino[:-1]
        lista.append(termino)
    return lista



'''
d = ["a", "a b", "c", "c a"]
d.sort()
t = ["b", "c", "d", "a", "c", "a"]
#t=["a","b"]
l = []



c = ComparadorCustomStems(d, t)
c.coincidencias()
print(c.getMatches())


'''









