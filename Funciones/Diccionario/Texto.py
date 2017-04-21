# -*- coding: utf-8 -*-

import re
from ProcesadorDeTexto import ProcesadorDeTexto

#n: file name
#p: path of the file
class Texto(ProcesadorDeTexto):
    def __init__(self,n,p):
        super(Texto, self).__init__(n,p)
        self.__words = []

    def clean(self):          
        self.text = re.sub(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"," ",self.text)
        self.text = re.sub(r"\d|[\t\r\n\f]+"," ",self.text) #espacios
        self.text = re.sub(r"[ ]+"," ",self.text) #multiples espacios
        self.text = self.text.lower()

    def loadWords(self):
        self.__words = self.text.split(" ")

    def getWords(self):
        return self.__words

'''
textPath =  r'C:\\Users\\Rayo1115\\Desktop\\Document classification\\raw data\\OPIA\\'
textFile = '3.txt'

texto = Texto(textFile, textPath)
texto.loadText()
texto.clean()
texto.loadWords()

arreglo = texto.getText().split(" ")
print(arreglo[0])
print(texto.getWords()[1])
'''
