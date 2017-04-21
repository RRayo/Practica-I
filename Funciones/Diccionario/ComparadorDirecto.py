# -*- coding: utf-8 -*-

from Diccionario import Diccionario
from Texto import Texto
from Funciones import binarySearchDicc

class ComparadorDirecto():
    def __init__(self,diccionario,texto):
        self.__texto = texto
        self.__diccionario = diccionario
        self.__lista = []

    def coincidencias(self):
        for indice in range(len(self.__texto)):
            binarySearchDicc(self.__texto, indice, self.__diccionario, self.__lista, comparador)

    def getMatches(self):
        self.__lista = list(set(self.__lista))
        self.__lista.sort()
        return self.__lista
        
    def nombre(self):
        return "Comparador de stems"

    def getStemsText(self):
        return self.__texto

    def getStemsDict(self):
        return self.__diccionario
    
def comparador(string1, string2):
    return string1 == string2






