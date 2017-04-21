# -*- coding: utf-8 -*-

from ProcesadorDeTexto import ProcesadorDeTexto

#n: file name
#p: path of the file
class Diccionario(ProcesadorDeTexto):
    def __init__(self,n,p):
        super(Diccionario, self).__init__(n,p)
        self.__words = []

    def clean(self, diccN=0):
        self.text = self.text.lower()

    def loadWords(self):
        self.__words = self.text.split('\n')
        #ordenar palabras
        self.__words = list(set(self.__words))
        self.__words.sort()


    def getWords(self):
        return self.__words

